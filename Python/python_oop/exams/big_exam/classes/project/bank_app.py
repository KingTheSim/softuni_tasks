from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    TYPE_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }

    TYPE_CLIENTS = {
        "Student": Student,
        "Adult": Adult,
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: [BaseLoan] = []
        self.clients: [BaseClient] = []
        self.loaned_number = 0
        self.loaned_sum = 0.00
        self.income_sum = 0.00

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.TYPE_LOANS:
            raise Exception("Invalid loan type!")
        else:
            self.loans.append(self.TYPE_LOANS[loan_type]())
            return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
        if client_type not in self.TYPE_CLIENTS:
            raise Exception("Invalid client type!")
        elif len(self.clients) == self.capacity:
            return "Not enough bank capacity."
        else:
            self.clients.append(self.TYPE_CLIENTS[client_type](client_name, client_id, income))
            return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> str:
        client = None
        for c in self.clients:
            if c.client_id == client_id:
                client = c
                break

        if (client.__class__.__name__ == "Student" and loan_type == "MortgageLoan") or \
                (client.__class__.__name__ == "Adult" and loan_type == "StudentLoan"):
            raise Exception("Inappropriate loan type!")

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                client.loans.append(loan)
                self.loans.remove(loan)
                self.loaned_number += 1
                self.loaned_sum += loan.amount
                return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str) -> str:
        client = None
        for c in self.clients:
            if c.client_id == client_id:
                client = c
                break
        else:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        else:
            self.clients.remove(client)
            return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:
        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        else:
            return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float) -> str:
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        else:
            return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self) -> str:
        cur_income = sum(c.income for c in self.clients)
        cur_interest = sum(c.interest for c in self.clients) if self.clients else 0.00
        average = (cur_interest / len(self.clients)) if self.clients else 0.00
        cur_loans = sum(loan.amount for loan in self.loans)

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {cur_income:.2f}\n" \
               f"Granted Loans: {self.loaned_number}, Total Sum: {self.loaned_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {cur_loans:.2f}\n" \
               f"Average Client Interest Rate: {average:.2f}"

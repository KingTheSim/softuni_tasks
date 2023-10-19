from abc import ABC, abstractmethod
from project.loans.base_loan import BaseLoan


class BaseClient(ABC):
    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans: [BaseLoan] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Client name cannot be empty!")
        else:
            self.__name = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value: str):
        if len(value) != 10:
            raise ValueError("Client ID should be 10 symbols long!")
        else:
            self.__client_id = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value: float):
        if value <= 0.00:
            raise ValueError("Income must be greater than zero!")
        else:
            self.__income = value

    @abstractmethod
    def increase_clients_interest(self):
        pass

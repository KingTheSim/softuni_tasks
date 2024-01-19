from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        cur_customer = ""
        for c in self.customers:
            if c.id == customer_id:
                cur_customer = c
                break

        cur_dvd = ""
        for d in self.dvds:
            if d.id == dvd_id:
                cur_dvd = d
                break

        if cur_dvd in cur_customer.rented_dvds:
            return f"{cur_customer.name} has already rented {cur_dvd.name}"

        elif cur_dvd.is_rented:
            return "DVD is already rented"

        elif cur_dvd.age_restriction > cur_customer.age:
            return f"{cur_customer.name} should be at least {cur_dvd.age_restriction} to rent this movie"

        else:
            cur_dvd.is_rented = True
            cur_customer.rented_dvds.append(cur_dvd)
            return f"{cur_customer.name} has successfully rented {cur_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        cur_customer = ""
        for c in self.customers:
            if c.id == customer_id:
                cur_customer = c
                break

        cur_dvd = ""
        for d in self.dvds:
            if d.id == dvd_id:
                cur_dvd = d
                break

        if cur_dvd in cur_customer.rented_dvds:
            cur_dvd.is_rented = False
            cur_customer.rented_dvds.remove(cur_dvd)
            return f"{cur_customer.name} has successfully returned {cur_dvd.name}"

        else:
            return f"{cur_customer.name} does not have that DVD"

    def __repr__(self) -> str:
        result = []
        for c in self.customers:
            result.append(f"{c}")

        for d in self.dvds:
            result.append(f"{d}")

        result = "\n".join(result)
        return f"{result}"

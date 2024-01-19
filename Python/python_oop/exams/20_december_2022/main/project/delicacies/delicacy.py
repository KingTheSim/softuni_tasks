from abc import ABC, abstractmethod


class Delicacy(ABC):
    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError
        else:
            self.__price = value

    @abstractmethod
    def details(self):
        pass

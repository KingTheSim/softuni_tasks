from abc import ABC, abstractmethod
from project.delicacies.delicacy import Delicacy


class Booth(ABC):
    PRICE_PER_PERSON = 0.00

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: [Delicacy] = []
        self.price_for_reservation = 0.00
        self.is_reserved = False
        self.accumulated = 0.00

    @abstractmethod
    def reserve(self, number_of_people:int) -> None:
        pass

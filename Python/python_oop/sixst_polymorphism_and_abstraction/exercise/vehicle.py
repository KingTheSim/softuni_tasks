from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def fuel_needed(self, distance: float) -> float:
        pass

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    def fuel_needed(self, distance: float) -> float:
        return distance * (self.fuel_consumption + 0.9)

    def drive(self, distance: float):
        required = self.fuel_needed(distance)
        if self.fuel_quantity >= required:
            self.fuel_quantity -= required

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def fuel_needed(self, distance: float) -> float:
        return distance * (self.fuel_consumption + 1.6)

    def drive(self, distance: float) -> None:
        required = self.fuel_needed(distance)
        if self.fuel_quantity >= required:
            self.fuel_quantity -= required

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
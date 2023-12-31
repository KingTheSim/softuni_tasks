class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int) -> None:
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers: int) -> None:
        if self.fuel_consumption * kilometers <= self.fuel:
            self.fuel -= self.fuel_consumption * kilometers
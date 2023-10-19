from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen

class ChristmasPastryShopApp:
    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    VALID_BOOTHS = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths: [Booth] = []
        self.delicacies: [Delicacy] = []
        self.income = 0.00

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        for d in self.delicacies:
            if d.name == name:
                raise Exception("{delicacy name} already exists!")

        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception("{type of delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.VALID_DELICACIES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        for b in self.booths:
            if b.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.VALID_BOOTHS[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        for b in self.booths:
            if not b.is_reserved and b.capacity >= number_of_people:
                b.reserve(number_of_people)
                return f"Booth {b.number} has been reserved for {number_of_people} people."

        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        booth = None
        for b in self.booths:
            if b.booth_number == booth_number:
                booth = b
                break
        else:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = None
        for d in self.delicacies:
            if d.name == delicacy_name:
                delicacy = d
                break
        else:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.accumulated +=
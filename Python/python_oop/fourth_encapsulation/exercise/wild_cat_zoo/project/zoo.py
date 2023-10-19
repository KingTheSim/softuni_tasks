from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget > price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals):
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        required = sum([w.salary for w in self.workers])
        if self.__budget >= required:
            self.__budget -= required
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        required = sum([a.money_for_care for a in self.animals])
        if self.__budget >= required:
            self.__budget -= required
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []

        for a in self.animals:
            if a.__class__.__name__ == "Lion":
                lions.append(f"{a}")
            elif a.__class__.__name__ == "Tiger":
                tigers.append(f"{a}")
            else:
                cheetahs.append(f"{a}")

        lions_c = len(lions)
        tigers_c = len(tigers)
        cheetahs_c = len(cheetahs)
        lions = "\n".join(lions)
        tigers = "\n".join(tigers)
        cheetahs = "\n".join(cheetahs)

        return f"You have {len(self.animals)} animals\n" \
               f"----- {lions_c} Lions:\n{lions}\n" \
               f"----- {tigers_c} Tigers:\n{tigers}\n" \
               f"----- {cheetahs_c} Cheetahs:\n{cheetahs}"

    def workers_status(self) -> str:
        keepers = []
        caretakers = []
        vets = []

        for w in self.workers:
            if w.__class__.__name__ == "Keeper":
                keepers.append(f"{w}")
            elif w.__class__.__name__ == "Caretaker":
                caretakers.append(f"{w}")
            else:
                vets.append(f"{w}")

        keepers_c = len(keepers)
        caretakers_c = len(caretakers)
        vets_c = len(vets)
        keepers = "\n".join(keepers)
        caretakers = "\n".join(caretakers)
        vets = "\n".join(vets)

        return f"You have {len(self.workers)} workers\n" \
               f"----- {keepers_c} Keepers:\n{keepers}\n" \
               f"----- {caretakers_c} Caretakers:\n{caretakers}\n" \
               f"----- {vets_c} Vets:\n{vets}"

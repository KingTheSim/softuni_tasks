from project.customer import Customer
from project.equipment import Equipment
from project.trainer import Trainer
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription

class Gym:
    def __init__(self) -> None:
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = ""
        result = []
        for s in self.subscriptions:
            if s.id == subscription_id:
                subscription = s
                result.append(f"{s}")
                break

        for c in self.customers:
            if c.id == subscription.customer_id:
                result.append(f"{c}")
                break

        for t in self.trainers:
            if t.id == subscription.trainer_id:
                result.append(f"{t}")
                break

        plan = ""
        for p in self.plans:
            if p.id == subscription.exercise_id:
                plan = p
                break

        for e in self.equipment:
            if e.id == plan.equipment_id:
                result.append(f"{e}")
                result.append(f"{plan}")
                break

        result = "\n".join(result)
        return result

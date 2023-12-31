class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def is_ordered(self) -> str:
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> None or str:
        if not self.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity

            else:
                self.ingredients[ingredient] = quantity

            self.price += quantity * price_per_quantity

        else:
            return self.is_ordered()

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> None or str:
        if not self.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

            elif self.ingredients[ingredient] < quantity:
                return f"Please check again the desired quantity of {ingredient}!"

            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * price_per_quantity

        else:
            return self.is_ordered()

    def make_order(self) -> str:
        self.ordered = True
        final_ingredients = ", ".join([f"{i}: {q}" for i, q in self.ingredients.items()])
        return f"You've ordered pizza {self.name}" \
               f" prepared with {final_ingredients} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)

print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))

margarita.remove_ingredient('cheese', 2, 1)

print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

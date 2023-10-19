from math import ceil, floor

# user input
days = int(input())
food_kg = int(input())
d_food = float(input())  # daily food intake by the dog
c_food = float(input())  # daily food intake by the cat
t_food_g = float(input())  # daily food intake by the turtle in grams

# logic
needs_d = d_food * days
needs_c = c_food * days
t_food = t_food_g / 1000
needs_t = t_food * days
needs_total = needs_d + needs_c + needs_t

# output
if food_kg >= needs_total:
    print(f"{floor(food_kg - needs_total)} kilos of food left.")
else:
    print(f"{ceil(needs_total - food_kg)} more kilos of food are needed.")

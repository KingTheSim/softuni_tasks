from math import floor, ceil

# known
# 40% of the harvest is used for wine
grapes_per_liter = 2.5

# user input
winery_area_cub_met = int(input())
grapes_per_cub_met = float(input())
needed_wine = int(input())
workers_number = int(input())

# logic
grapes_produced = winery_area_cub_met * grapes_per_cub_met
grapes_for_wine = grapes_produced * 0.4
wine_produced = grapes_for_wine / grapes_per_liter

# code output
if wine_produced < needed_wine:
    print(f"It will be a tough winter! More {floor(needed_wine - wine_produced)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(wine_produced - needed_wine)} liters left -> "
          f"{ceil((wine_produced - needed_wine) / workers_number)} liters per person.")

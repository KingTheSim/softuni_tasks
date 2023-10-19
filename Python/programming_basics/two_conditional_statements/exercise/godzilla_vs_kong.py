# user input
movie_budget = float(input())
statists = int(input())
clothing_price = float(input())

# logic
decor = movie_budget * 0.1
clothing_sum = statists * clothing_price

if statists > 150:
    clothing_sum -= clothing_sum * 0.1

needed_budget = decor + clothing_sum

# code output
if needed_budget > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {needed_budget - movie_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - needed_budget:.2f} leva left.")

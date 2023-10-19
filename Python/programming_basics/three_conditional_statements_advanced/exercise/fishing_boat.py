# user input
budget = int(input())
season = input()
crew_num = int(input())

# logic
price = 0
if season in ["Spring"]:
    price = 3000
elif season in ["Autumn", "Summer"]:
    price = 4200
else:
    price = 2600

if crew_num <= 6:
    price = price * 0.90
elif 6 < crew_num <= 11:
    price = price * 0.85
else:
    price = price * 0.75

if season != "Autumn":
    if crew_num % 2 == 0:
        price = price * 0.95
diff = abs(budget - price)

# code output
if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

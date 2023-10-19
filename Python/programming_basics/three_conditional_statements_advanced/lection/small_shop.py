# user input
stock = input()
city = input()
amount = float(input())

# logic
price = 0
if city == "Sofia":
    if stock == "coffee":
        price = 0.50
    elif stock == "water":
        price = 0.8
    elif stock == "beer":
        price = 1.20
    elif stock == "sweets":
        price = 1.45
    else:
        price = 1.60
elif city == "Plovdiv":
    if stock == "coffee":
        price = 0.40
    elif stock == "water":
        price = 0.70
    elif stock == "beer":
        price = 1.15
    elif stock == "sweets":
        price = 1.30
    else:
        price = 1.50
elif city == "Varna":
    if stock == "coffee":
        price = 0.45
    elif stock == "water":
        price = 0.70
    elif stock == "beer":
        price = 1.10
    elif stock == "sweets":
        price = 1.35
    else:
        price = 1.55

total = amount * price

# code output
print(total)

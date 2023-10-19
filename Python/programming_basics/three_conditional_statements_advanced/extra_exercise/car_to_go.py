# user input
budget = float(input())
season = input()

# logic
price_car = 0
class_car = ""
type_car = ""

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.35
    else:
        type_car = "Jeep"
        price_car = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.45
    else:
        type_car = "Jeep"
        price_car = budget * 0.80
else:
    class_car = "Luxury class"
    type_car = "Jeep"
    price_car = budget * 0.90

# code output
print(f"{class_car}")
print(f"{type_car} - {price_car:.2f}")

# user input
fuel_type = input()
fuel_amount = float(input())

# logic
if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if fuel_amount >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")

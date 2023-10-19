# user input
budget = float(input())
season = input()

# logic
price = 0
sleep = ""
destination = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        sleep = "Camp"
        price = budget * 0.30
    else:
        sleep = "Hotel"
        price = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        sleep = "Camp"
        price = budget * 0.40
    else:
        sleep = "Hotel"
        price = budget * 0.80
else:
    destination = "Europe"
    price = budget * 0.90
    sleep = "Hotel"

# code output
print(f"Somewhere in {destination}")
print(f"{sleep} - {price:.2f}")

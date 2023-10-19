# user input
budget = float(input())
season = input()

# logic
location = ""
sleep = ""
price = 0

if budget <= 1000:
    sleep = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    sleep = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    else:
        location = "Morocco"
        price = budget * 0.60
else:
    sleep = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    else:
        location = "Morocco"
        price = budget * 0.90

# code output
print(f"{location} - {sleep} - {price:.2f}")

# user input
season = input()
km = float(input())

# logic
salary = 0
taxes = 0.90
if km <= 5000:
    if season in ["Spring", "Autumn"]:
        salary = 0.75 * km * taxes * 4
    elif season == "Summer":
        salary = 0.90 * km * taxes * 4
    else:
        salary = 1.05 * km * taxes * 4
elif 5000 < km <= 10000:
    if season in ["Spring", "Autumn"]:
        salary = 0.95 * km * taxes * 4
    elif season == "Summer":
        salary = 1.10 * km * taxes * 4
    else:
        salary = 1.25 * km * taxes * 4
elif 10000 < km <= 20000:
    salary = 1.45 * km * taxes * 4

# code output
print(f"{salary:.2f}")

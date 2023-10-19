# user input
inheritance = float(input())
target_year = int(input())

# logic
cash = inheritance
age = 0
for i in range(1800, target_year + 1):
    if i == 1800:
        cash -= 12000
        age = 18
    elif i % 2 == 0:
        cash -= 12000
        age += 1
    else:
        age += 1
        cash -= 12000 + (50 * age)

# code output
if cash >= 0:
    print(f"Yes! He will live a carefree life and will have {cash:.2f} dollars left.")
else:
    cash = abs(cash)
    print(f"He will need {cash:.2f} dollars to survive.")

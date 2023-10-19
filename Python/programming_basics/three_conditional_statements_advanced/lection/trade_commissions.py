# user input
city = input()
amount = float(input())

# logic
if 0 <= amount <= 500:
    if city == "Sofia":
        print(f"{(amount * 0.05):.2f}")
    elif city == "Varna":
        print(f"{(amount * 0.045):.2f}")
    elif city == "Plovdiv":
        print(f"{(amount * 0.055):.2f}")
    else:
        print("error")
elif 500 < amount <= 1000:
    if city == "Sofia":
        print(f"{(amount * 0.07):.2f}")
    elif city == "Varna":
        print(f"{(amount * 0.075):.2f}")
    elif city == "Plovdiv":
        print(f"{(amount * 0.08):.2f}")
    else:
        print("error")
elif 1000 < amount <= 10000:
    if city == "Sofia":
        print(f"{(amount * 0.08):.2f}")
    elif city == "Varna":
        print(f"{(amount * 0.10):.2f}")
    elif city == "Plovdiv":
        print(f"{(amount * 0.12):.2f}")
    else:
        print("error")
elif amount > 10000:
    if city == "Sofia":
        print(f"{(amount * 0.12):.2f}")
    elif city == "Varna":
        print(f"{(amount * 0.13):.2f}")
    elif city == "Plovdiv":
        print(f"{(amount * 0.145):.2f}")
    else:
        print("error")
else:
    print("error")

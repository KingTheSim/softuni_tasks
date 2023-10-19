# user input
age = float(input())
sex = input()

# logic
if sex == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
else:
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

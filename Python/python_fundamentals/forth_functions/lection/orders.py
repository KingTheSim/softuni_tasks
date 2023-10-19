def calc(order, number):
    if order == "coffee":
        return number * 1.50
    elif order == "coke":
        return number * 1.40
    elif order == "water":
        return float(number)
    elif order == "snacks":
        return number * 2.00


order = input()
n = int(input())

print(f"{calc(order, n):.2f}")

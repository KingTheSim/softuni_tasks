products = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    if name not in products:
        products[name] = [0, 0]
    products[name][0] = float(price)
    products[name][1] += int(quantity)

for key in products:
    print(f"{key} -> {(products[key][0] * products[key][1]):.2f}")

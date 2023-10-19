stock = {}
while True:
    current = input()

    if current == "statistics":
        break

    key, quantity = current.split(": ")
    if key not in stock:
        stock[key] = 0
    stock[key] += int(quantity)

print("Products in stock:")
for (key, quantity) in stock.items():
    print(f"- {key}: {quantity}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")

orders = int(input())

total = 0
for _ in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 > capsule_price or 100 < capsule_price:
        continue
    if 1 > days or 31 < days:
        continue
    if 1 > capsules or 2000 < capsules:
        continue
    price = capsule_price * days * capsules
    print(f"The price for the coffee is: ${price:.2f}")
    total += price

print(f"Total: ${total:.2f}")

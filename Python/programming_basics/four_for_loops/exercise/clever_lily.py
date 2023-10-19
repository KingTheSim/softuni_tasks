# user input
age = int(input())
targe = float(input())
toy_price = int(input())

# logic
cash = 0
total = 0
toy_count = 0
brother = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        cash = cash + 10
        total += cash
        brother += 1
    else:
        toy_count += 1

toy_cash = toy_price * toy_count
total_cash = toy_cash + total - brother
diff = abs(total_cash - targe)
# code output
if total_cash >= targe:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

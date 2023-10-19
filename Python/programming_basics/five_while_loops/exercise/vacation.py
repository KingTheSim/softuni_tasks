# user input
cash_target = float(input())
cash_start = float(input())

# logic
total_cash = cash_start
spend_count = 0
days_count = 0
target = False
while True:
    transaction = input()
    cash = float(input())
    days_count += 1
    if transaction == "spend":
        total_cash -= cash
        if total_cash < 0:
            total_cash = 0
        spend_count += 1
    else:
        total_cash += cash
        spend_count = 0
    if spend_count == 5:
        break
    if total_cash >= cash_target:
        target = True
        break
# code output
if target:
    print(f"You saved the money for {days_count} days.")
else:
    print("You can't save the money.")
    print(f"{days_count}")

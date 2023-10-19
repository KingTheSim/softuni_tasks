# user input
target = int(input())

# logic
count = 0
count_cash = 0
count_card = 0
cash = 0
cash_money = 0
cash_card = 0
cs = 0
cc = 0
while True:
    comm = input()
    if comm == "End":
        print("Failed to collect required money for charity.")
        break
    current_cash = float(comm)
    count += 1
    if count % 2 != 0:
        if current_cash > 100:
            print("Error in transaction!")
        else:
            count_cash += 1
            cash += current_cash
            cash_money += current_cash
            print("Product sold!")
    else:
        if current_cash < 10:
            print("Error in transaction!")
        else:
            count_card += 1
            cash += current_cash
            cash_card += current_cash
            print("Product sold!")
    if cash >= target:
        cs = cash_money / count_cash
        cc = cash_card / count_card
        print(f"Average CS: {cs:.2f}")
        print(f"Average CC: {cc:.2f}")
        break

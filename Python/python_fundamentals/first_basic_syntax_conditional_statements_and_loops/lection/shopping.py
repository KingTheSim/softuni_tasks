budget = int(input())

cash = 0
overdraft = False
while True:
    price = input()
    if price == "End":
        break
    else:
        price = int(price)
    cash += price
    if cash > budget:
        overdraft = True
        break

if overdraft:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")

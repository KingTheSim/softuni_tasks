budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25

price_bread = flour_price + egg_price + milk_price

coloured_eggs = 0
counter = 0
cash = budget
while True:
    if price_bread > cash:
        flag = True
        break
    counter += 1
    coloured_eggs += 3
    if counter % 3 == 0:
        coloured_eggs -= counter - 2
    cash -= price_bread

print(f"You made {counter} loaves of Easter bread! Now you have {coloured_eggs} eggs and {cash:.2f}BGN left.")

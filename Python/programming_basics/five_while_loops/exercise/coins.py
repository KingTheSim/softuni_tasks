# user input
leva = float(input())

# logic
coins = leva * 100
coins_count = 0
while coins > 0:
    if coins >= 200:
        coins -= 200
    elif coins >= 100:
        coins -= 100
    elif coins >= 50:
        coins -= 50
    elif coins >= 20:
        coins -= 20
    elif coins >= 10:
        coins -= 10
    elif coins >= 5:
        coins -= 5
    elif coins >= 2:
        coins -= 2
    elif coins >= 1:
        coins -= 1
    else:
        break
    coins_count += 1

# code output
print(coins_count)

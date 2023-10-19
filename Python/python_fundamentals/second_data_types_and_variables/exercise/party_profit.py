start_group = int(input())
days = int(input())

group = start_group
coins = 0
for i in range(1, days + 1):
    if i % 10 == 0:
        group -= 2
    if i % 15 == 0:
        group += 5
        coins -= group * 2
    coins += 50 - (2 * group)
    if i % 3 == 0:
        coins -= 3 * group
    if i % 5 == 0:
        coins += 20 * group

coins_per_companion = coins // group
print(f"{group} companions received {coins_per_companion} coins each.")

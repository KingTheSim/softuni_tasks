quantity = int(input())
days = int(input())

cash = 0
points = 0
cur_quantity = quantity
for i in range(1, days + 1):
    if i == days and days % 10 == 0:
        points -= 30
    if i % 10 == 0:
        points -= 20
        cash += 5 + 3 + 15
    if i % 11 == 0:
        cur_quantity += 2
    if i % 2 == 0:
        cash += cur_quantity * 2
        points += 5
    if i % 3 == 0:
        cash += (cur_quantity * 5) + (cur_quantity * 3)
        points += (3 + 10)
    if i % 5 == 0:
        cash += cur_quantity * 15
        points += 17
    if i % 5 == 0 and i % 3 == 0:
        points += 30

print(f"Total cost: {cash}")
print(f"Total spirit: {points}")

losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

helmet = 0
sword = 0
shield = 0
armour = 0
counter = 0
for i in range(1, losses + 1):
    if i % 2 == 0:
        helmet += 1
    if i % 3 == 0:
        sword += 1
    if i % 6 == 0:
        shield += 1
        counter += 1
    if counter == 2:
        armour += 1
        counter = 0

result = helmet * helmet_price + sword * sword_price + shield * shield_price + armour * armour_price
print(f"Gladiator expenses: {result:.2f} aureus")

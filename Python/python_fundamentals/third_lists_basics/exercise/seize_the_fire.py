cells = input().split("#")
water = int(input())

total = 0
watered = []
for cell in cells:
    current = cell.split(" = ")
    value = int(current[1])
    if current[0] == "High" and (81 > value or 125 < value):
        continue
    elif current[0] == "Medium" and (51 > value or 80 < value):
        continue
    elif current[0] == "Low" and (1 > value or 50 < value):
        continue

    if total + value > water:
        continue
    total += value
    watered.append(value)

print("Cells:")
for cell in watered:
    print(f"- {cell}")
effort = total * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total}")

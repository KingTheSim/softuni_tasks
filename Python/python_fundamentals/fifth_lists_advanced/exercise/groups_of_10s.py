numbers = [int(x) for x in input().split(", ")]

current_lower = 1
current_roof = 10
current_numbers = numbers
new_numbers = numbers
while new_numbers:
    print(f"Group of {current_roof}'s: {[a for a in current_numbers if 1 <= a <= current_roof]}")
    current_numbers = []
    for i in numbers:
        if i > current_roof:
            current_numbers.append(i)
    new_numbers = [b for b in numbers if b in current_numbers]
    current_lower += 10
    current_roof += 10

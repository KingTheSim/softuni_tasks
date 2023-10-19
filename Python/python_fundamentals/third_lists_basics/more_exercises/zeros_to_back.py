numbers = [int(x) for x in input().split(", ")]

for i in numbers:
    if i == 0:
        numbers.remove(0)
        numbers.append(0)

print(numbers)

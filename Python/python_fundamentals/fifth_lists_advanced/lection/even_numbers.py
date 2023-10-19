numbers = [int(x) for x in input().split(", ")]

indexes = [x for x in range(len(numbers)) if numbers[x] % 2 == 0]
print(indexes)

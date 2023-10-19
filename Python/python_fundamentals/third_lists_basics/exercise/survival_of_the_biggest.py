numbers = [int(x) for x in input().split()]
target = int(input())

for _ in range(target):
    numbers.remove(min(numbers))

for i in numbers:
    if i == numbers[-1]:
        print(i)
    else:
        print(i, end=", ")

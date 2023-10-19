def evener(num):
    return num % 2 == 0


numbers = [int(x) for x in input().split()]

print(list(filter(evener, numbers)))

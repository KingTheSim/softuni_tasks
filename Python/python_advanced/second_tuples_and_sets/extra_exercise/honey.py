from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())
honey = 0

making = {
    "+": lambda x, y:  x + y,
    "-": lambda x, y:  x - y,
    "*": lambda x, y:  x * y,
    "/": lambda x, y:  x / y,
}

while bees and nectar:
    cur_bee = bees.popleft()
    cur_nectar = nectar.pop()

    if cur_nectar < cur_bee:
        bees.appendleft(cur_bee)
    elif cur_nectar > cur_bee:
        honey += abs(making[symbols.popleft()](cur_bee, cur_nectar))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(y) for y in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(y) for y in nectar)}")

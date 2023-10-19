from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
waste = 0
cur_cup = 0
cur_bottle = 0

while bottles:
    if cur_cup == 0 and cups:
        cur_cup = cups.popleft()
    elif cur_cup == 0 and not cups:
        print(f"Bottles: {' '.join([str(x) for x in bottles])}")
        break
    cur_bottle = bottles.pop()

    if cur_bottle <= cur_cup:
        cur_cup -= cur_bottle
        continue
    else:
        waste += cur_bottle - cur_cup
        cur_cup = 0

else:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {waste}")

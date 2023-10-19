from collections import deque

choco = deque([int(x) for x in input().split(", ")])
milks = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while choco and milks and milkshakes != 5:
    cur_milk = milks.popleft()
    cur_choco = choco.pop()

    if cur_milk <= 0 and cur_choco <= 0:
        continue
    elif cur_choco <= 0:
        milks.appendleft(cur_milk)
    elif cur_milk <= 0:
        choco.append(cur_choco)

    elif cur_milk == cur_choco:
        milkshakes += 1
    else:
        milks.append(cur_milk)
        choco.append(cur_choco - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(x) for x in choco]) if choco else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in milks]) if milks else 'empty'}")

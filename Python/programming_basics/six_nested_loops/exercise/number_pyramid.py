n = int(input())
current = 0
reached = False
for row in range(1, n + 1):
    for coll in range(1, row + 1):
        current += 1
        print(current, end=" ")
        if current == n:
            reached = True
            break
    if reached:
        break
    print()

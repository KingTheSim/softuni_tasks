from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))
for client in orders.copy():

    if food >= client:
        food -= client
        orders.popleft()

    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break

else:
    print("Orders complete")

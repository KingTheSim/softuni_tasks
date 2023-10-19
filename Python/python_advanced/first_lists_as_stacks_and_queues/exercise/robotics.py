from datetime import datetime, timedelta
from collections import deque

robots = {}
for r in input().split(";"):
    name, pr_time = r.split("-")
    robots[name] = [int(pr_time), 0]

start = datetime.strptime(input(), "%H:%M:%S")

items = deque()
while True:
    item = input()
    if item == "End":
        break
    else:
        items.append(item)

while items:
    start += timedelta(0, 1)
    cur = items.popleft()

    vacant = []
    for name, var in robots.items():
        if var[1] != 0:
            var[1] -= 1

        if var[1] == 0:
            vacant.append(name)

    if not vacant:
        items.append(cur)
    else:
        robots[vacant[0]][1] = robots[vacant[0]][0]
        print(f"{vacant[0]} - {cur} [{start.strftime('%H:%M:%S')}]")

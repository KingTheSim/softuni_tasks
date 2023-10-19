from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_cap = int(input())

racks = 1
cur_rack = 0
while clothes:
    item = clothes.popleft()

    if cur_rack + item > rack_cap:
        racks += 1
        cur_rack = 0
        cur_rack += item

    else:
        cur_rack += item

print(racks)

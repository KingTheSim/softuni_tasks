
from collections import deque
line = deque(input().split())

cur_nums = deque()

funcs = {
    "+": lambda length: [cur_nums.appendleft(cur_nums.popleft() + cur_nums.popleft()) for _ in range(length - 1)],
    "-": lambda length: [cur_nums.appendleft(cur_nums.popleft() - cur_nums.popleft()) for _ in range(length - 1)],
    "*": lambda length: [cur_nums.appendleft(cur_nums.popleft() * cur_nums.popleft()) for _ in range(length - 1)],
    "/": lambda length: [cur_nums.appendleft(cur_nums.popleft() // cur_nums.popleft()) for _ in range(length - 1)],
}

while line:
    cur = line.popleft()

    if cur.isdigit() or len(cur) != 1:
        cur_nums.append(int(cur))
    else:
        if len(cur_nums) == 1:
            continue

        funcs[cur](len(cur_nums))

else:
    print(cur_nums.pop())

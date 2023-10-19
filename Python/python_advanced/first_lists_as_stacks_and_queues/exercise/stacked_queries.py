from collections import deque

nums = deque()

functions = {
    1: lambda x: nums.append(x[1]),
    2: lambda x: nums.pop() if nums else None,
    3: lambda x: print(max(nums)) if nums else None,
    4: lambda x: print(min(nums)) if nums else None,
}

for _ in range(int(input())):
    raw_command = [int(x) for x in input().split()]
    functions[raw_command[0]](raw_command)


nums.reverse()
print(*nums, sep=", ")

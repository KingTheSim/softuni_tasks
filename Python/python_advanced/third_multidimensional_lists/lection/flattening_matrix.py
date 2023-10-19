matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]
flattened = []
[flattened.extend(a) for a in matrix]
print(flattened)


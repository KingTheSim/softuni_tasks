n = int(input())

for a in range(1, n + 1):
    for b in range(a):
        print("*", end="")
    print()

for c in range(n - 1, 0, -1):
    for d in range(c):
        print("*", end="")
    print()

n = int(input())

for a in range(1, n + 1):
    print("*", end="")
print()
counter = 0

while True:
    if n == 2:
        break
    counter += 1
    for c in range(1, n + 1):
        if c == 1 or c == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    if counter == n - 2:
        break

for d in range(1, n + 1):
    print("*", end="")

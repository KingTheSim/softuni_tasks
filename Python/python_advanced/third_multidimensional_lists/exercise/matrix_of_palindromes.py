rows, cols = [int(x) for x in input().split()]
start = ord("a")

for r in range(rows):
    for c in range(r, cols + r):
        print(f"{chr(start + r)}{chr(start + c)}{chr(start + r)}", end=" ")

    print()
    
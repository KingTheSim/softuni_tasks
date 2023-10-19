lists = input().split("|")

matrix = [x.split() for x in lists]
for r in matrix[::-1]:
    if r:
        print(" ".join(r), end=" ")

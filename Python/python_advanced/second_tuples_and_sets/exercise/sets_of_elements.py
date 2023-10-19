n, m = [int(x) for x in input().split()]

first = {input() for _ in range(n)}
second = {input() for _ in range(m)}

intersect = first.intersection(second)
print(*intersect, sep="\n")

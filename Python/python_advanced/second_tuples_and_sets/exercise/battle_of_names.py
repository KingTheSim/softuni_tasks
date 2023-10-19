odds = set()
evens = set()

for i in range(int(input())):
    cur_name_int = int(sum(ord(x) for x in input()) / (i + 1))
    if cur_name_int % 2 == 0: evens.add(cur_name_int)
    else: odds.add(cur_name_int)

if sum(odds) == sum(evens):
    print(*odds.union(evens), sep=", ")
elif sum(odds) > sum(evens):
    print(*odds.difference(evens), sep=", ")
else:
    print(*odds.symmetric_difference(evens), sep=", ")

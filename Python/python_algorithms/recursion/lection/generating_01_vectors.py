def recurser(current, inx):
    if inx == len(current):
        print(*current, sep="")
        return

    for i in range(2):
        current[inx] = i
        recurser(current, inx + 1)


bits = int(input())

empty = [0] * bits
recurser(empty, 0)

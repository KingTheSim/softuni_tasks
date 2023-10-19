def reverse_printer(group, inx):
    if inx == len(group) - 1:
        print(group[inx], end=" ")
        return
    else:
        reverse_printer(group, inx + 1)
        print(group[inx], end=" ")
        return


arr = [int(x) for x in input().split()]

reverse_printer(arr, 0)

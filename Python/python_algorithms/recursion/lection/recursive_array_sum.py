def summer(numbers, inx):
    if inx == len(numbers) - 1:
        return numbers[inx]
    return numbers[inx] + summer(numbers, inx + 1)


arr = [int(x) for x in input().split()]

print(summer(arr, 0))

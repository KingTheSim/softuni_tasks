numbers = int(input())

for i in range(1, numbers + 1):
    sum_number = 0
    special = False
    i_string = str(i)
    for a in i_string:
        sum_number += int(a)
    if sum_number in [5, 7, 11]:
        special = True
    print(f"{i} -> {special}")

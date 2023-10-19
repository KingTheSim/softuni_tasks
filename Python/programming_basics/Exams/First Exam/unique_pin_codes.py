n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

counter = 0
for a in range(1, n_1 + 1):
    for b in range(1, n_2 + 1):
        for c in range(1, n_3 + 1):
            flag_second = False
            if b in [2, 3, 5, 7]:
                flag_second = True
            if a % 2 == 0 and c % 2 == 0 and flag_second:
                print(f"{a} {b} {c}")

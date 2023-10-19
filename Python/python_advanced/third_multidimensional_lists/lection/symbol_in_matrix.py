SIZE = int(input())
matrix = [list(input()) for _ in range(SIZE)]
target = input()

for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == target:
            print(f"({row}, {col})")
            exit()
else:
    print(f"{target} does not occur in the matrix")

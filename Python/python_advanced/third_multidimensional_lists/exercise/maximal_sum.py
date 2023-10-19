rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
maximal_result = float("-inf")
maximal_local = []

for r in range(rows - 2):
    for c in range(cols - 2):
        first_row = matrix[r][c:c + 3]
        second_row = matrix[r + 1][c:c + 3]
        third_row = matrix[r + 2][c:c + 3]

        cur_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if cur_sum > maximal_result:
            maximal_result = cur_sum
            maximal_local = [first_row, second_row, third_row]

print(f"Sum = {maximal_result}")
for i in range(len(maximal_local)):
    print(*maximal_local[i], sep=" ")


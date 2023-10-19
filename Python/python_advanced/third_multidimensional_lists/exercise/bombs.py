size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

bombs_coordinates = [[int(x) for x in x.split(",")] for x in input().split()]

directions = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 0)
)

for row, col in bombs_coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        new_row, new_col = row + x, col + y

        if 0 <= new_row < size and 0 <= new_col < size:
            matrix[new_row][new_col] -= matrix[row][col] if matrix[new_row][new_col] > 0 else 0

# for row in matrix:
#     for num in row:
#         if num > 0:
#             alive_cells.append(num)

alive_cells = [num for row in matrix for num in row if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*rows) for rows in matrix]
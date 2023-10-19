size = int(input())

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
start = ()

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "B":
            start = (row, col)

path_of_bunny = []
collected_eggs = 0
final_direction = ""

for direction, position in directions.items():

    current_path = []
    current_eggs = 0

    row, col = start[0] + position[0], start[1] + position[1]

    while 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == "X":
            break

        current_path.append([row, col])
        current_eggs += int(matrix[row][col])

        row += position[0]
        col += position[1]

    if current_eggs >= collected_eggs:
        collected_eggs = current_eggs
        path_of_bunny = current_path
        final_direction = direction

print(final_direction)
print(*path_of_bunny, sep="\n")
print(collected_eggs)

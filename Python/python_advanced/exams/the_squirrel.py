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
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "s":
            start = (row, col)
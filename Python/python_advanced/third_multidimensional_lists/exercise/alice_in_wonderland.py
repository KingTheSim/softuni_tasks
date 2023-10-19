def valid_idx(row, col):
    return 0 <= row < size and 0 <= col < size


size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]

tea = 0
alice = ()
commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "A":
            alice = (row, col)
            matrix[row][col] = "*"

new_row, new_col = alice[0], alice[1]
while True:
    if tea >= 10:
        break
    command = input()

    new_row, new_col = new_row + commands[command][0], new_col + commands[command][1]
    if not valid_idx(new_row, new_col):
        break

    if matrix[new_row][new_col] == "R":
        matrix[new_row][new_col] = "*"
        break

    if matrix[new_row][new_col].isdigit():
        tea += int(matrix[new_row][new_col])

    matrix[new_row][new_col] = "*"

if tea < 10:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

[print(*row) for row in matrix]
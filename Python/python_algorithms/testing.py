from collections import deque

size = int(input())
commands = deque(input().split())
ending = False
matrix = list([[x for x in input().split()] for _ in range(size)])
total_coals = len([[el for el in matrix[x] if el == "c"] for x in range(size)]) - 1

end = set()
start = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

found = False
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "s":
            start = (row, col)
            found = True
            break

    if found:
        break

miner_move_row, miner_move_col = start[0], start[1]

while commands:
    command = commands.popleft()
    miner_move_row, miner_move_col = miner_move_row + directions[command][0], miner_move_col + directions[command][1]
    if 0 <= miner_move_row < size and 0 <= miner_move_col < size:
        element = matrix[miner_move_row][miner_move_col]

        if element == "c":

            total_coals -= 1
            matrix[miner_move_row][miner_move_col] = "*"
            if total_coals == 0:
                print(f"You collected all coal! {miner_move_row, miner_move_col}")
                break
        elif element == "e":
            print(f"Game over! {miner_move_row, miner_move_col}")
            break

else:
    print(f"{total_coals} pieces of coal left. {miner_move_row, miner_move_col}")

# for row in range(size):
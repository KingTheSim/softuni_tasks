def valid_idx(row, col):
    return 0 <= row < 5 and 0 <= col < 5


matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
counter = 0
shoots = 0
start = ()
shoot_x = []
for rows in range(5):
    matrix.append(input().split())
    for cols in range(5):
        if matrix[rows][cols] == "A":
            start = (rows, cols)
            matrix[rows][cols] = "."

        elif matrix[rows][cols] == "x":
            counter += 1

for _ in range(int(input())):
    new_rows, new_cols = start
    command = input().split()

    if command[0] == "move":

        new_rows = directions[command[1]][0] * int(command[2]) + start[0]
        new_cols = directions[command[1]][1] * int(command[2]) + start[1]

        if valid_idx(new_rows, new_cols):

            if matrix[new_rows][new_cols] == ".":
                start = new_rows, new_cols

    elif command[0] == "shoot":
        direction = command[1]
        row_shoot = directions[command[1]][0] + start[0]
        col_shoot = directions[command[1]][1] + start[1]

        while valid_idx(row_shoot, col_shoot):
            if matrix[row_shoot][col_shoot] == "x":
                matrix[row_shoot][col_shoot] = "."
                shoots += 1
                shoot_x.append([row_shoot, col_shoot])

                break
            row_shoot += directions[command[1]][0]
            col_shoot += directions[command[1]][1]

        if shoots == counter:
            print(f"Training completed! All {counter} targets hit.")
            break

else:
    print(f"Training not completed! {counter - shoots} targets left.")

print(*[x for x in shoot_x], sep='\n')

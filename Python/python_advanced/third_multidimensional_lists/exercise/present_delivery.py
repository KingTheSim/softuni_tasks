presents = int(input())
size = int(input())

nice = 0
all_nice_kids = 0
matrix = []
start = ()

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "S":
            start = row, col
            matrix[row][col] = '-'
        elif matrix[row][col] == "V":
            all_nice_kids += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

new_row, new_col = start[0], start[1]
while True:
    command = input()

    if command == "Christmas morning":
        break

    new_row += directions[command][0]
    new_col += directions[command][1]

    if matrix[new_row][new_col] == "X":
        matrix[new_row][new_col] = "-"
    elif matrix[new_row][new_col] == "V":
        matrix[new_row][new_col] = "-"
        nice += 1
        presents -= 1
    elif matrix[new_row][new_col] == "C":
        matrix[new_row][new_col] = "-"
        for direct, position in directions.items():
            row_drugs, col_drugs = new_row + position[0], new_col + position[1]

            if matrix[row_drugs][col_drugs] != "-":
                if matrix[row_drugs][col_drugs] == "V":
                    nice += 1
                matrix[row_drugs][col_drugs] = "-"
                presents -= 1
            if presents == 0:
                break

    if nice == all_nice_kids:
        break

    if presents <= 0:
        print(f"Santa ran out of presents!")
        break

matrix[new_row][new_col] = "S"

[print(*row) for row in matrix]

if nice == all_nice_kids:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {all_nice_kids - nice} nice kid/s.")

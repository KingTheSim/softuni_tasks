def move_validator(row, col, rows, cols):
    if row > rows or col > cols:
        return False
    else:
        return True


def path_calculator(row, col, rows, cols):
    if row == rows and col == cols:
        return 1
    else:
        if move_validator(row, col, rows, cols):
            moves = 0
            moves += path_calculator(row + 1, col, rows, cols)
            moves += path_calculator(row, col + 1, rows, cols)
            return moves
        else:
            return 0


m = int(input())
n = int(input())

print(path_calculator(1, 1, m, n))

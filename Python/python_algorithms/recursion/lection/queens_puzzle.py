def printer(current):
    for row in current:
        print(" ".join(row))
    print()


def place_validator(row, col, rows, cols, left_diags, right_diags):
    if row in rows or col in cols or row > 7 or col > 7:
        return False
    elif (row - col) in left_diags:
        return False
    elif (row + col) in right_diags:
        return False
    else:
        return True


def setter(cur_row, column, table, rows, cols, left_diagonals, right_diagonals):
    table[cur_row][column] = "*"
    rows.add(cur_row)
    cols.add(column)
    left_diagonals.add(cur_row - column)
    right_diagonals.add(cur_row + column)


def remover(cur_row, column, table, rows, cols, left_diagonals, right_diagonals):
    table[cur_row][column] = "-"
    rows.remove(cur_row)
    cols.remove(column)
    left_diagonals.remove(cur_row - column)
    right_diagonals.remove(cur_row + column)


def solver(cur_row, table, rows, cols, left_diagonals, right_diagonals):
    if cur_row == 8:
        printer(table)
        return
    for column in range(8):
        if place_validator(cur_row, column, rows, cols, left_diagonals, right_diagonals):
            setter(cur_row, column, table, rows, cols, left_diagonals, right_diagonals)
            solver(cur_row + 1, table, rows, cols, left_diagonals, right_diagonals)
            remover(cur_row, column, table, rows, cols, left_diagonals, right_diagonals)


n = 8
board = []
[board.append(["-"] * n) for _ in range(8)]

solver(0, board, set(), set(), set(), set())

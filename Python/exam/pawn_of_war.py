def validator(row, col):
    return 0 <= row <= 7 and 0 <= col <= 7


def mover(row, col, old_row, old_col):
    if board[row][col] == "w":
        global white
        white = ()
    elif board[row][col] == "b":
        global black
        black = ()
    board[row][col] = board[old_row][old_col]
    board[old_row][old_col] = "-"
    return row, col


def checker(row, col, piece, matrix):
    if piece == "w":
        if validator(row - 1, col - 1) and matrix[row - 1][col - 1] == "b":
            return mover(row - 1, col - 1, row, col)
        elif validator(row - 1, col + 1) and matrix[row - 1][col + 1] == "b":
            return mover(row - 1, col + 1, row, col)
        else:
            return mover(row - 1, col, row, col)
    else:
        if validator(row + 1, col - 1) and matrix[row + 1][col - 1] == "w":
            return mover(row + 1, col - 1, row, col)
        elif validator(row + 1, col + 1) and matrix[row + 1][col + 1] == "w":
            return mover(row + 1, col + 1, row, col)
        else:
            return mover(row + 1, col, row, col)


SIZE = 8

board = []
white = ()
black = ()
for i in range(SIZE):
    current = input().split()
    if "w" in current:
        white = (i, current.index("w"))
    if "b" in current:
        black = (i, current.index("b"))
    board.append(current)

while white and black:
    white = checker(*white, "w", board)
    if white[0] == 0:
        break
    if black:
        black = checker(*black, "b", board)
        if black[0] == 7:
            break

if white and not black:
    square = f"{chr(white[1] + 97)}{8 - white[0]}"
    print(f"Game over! White win, capture on {square}.")
elif black and not white:
    square = f"{chr(black[1] + 97)}{8 - black[0]}"
    print(f"Game over! Black win, capture on {square}.")
elif white[0] == 0:
    square = f"{chr(white[1] + 97)}{8 - white[0]}"
    print(f"Game over! White pawn is promoted to a queen at {square}.")
else:
    square = f"{chr(black[1] + 97)}{8 - black[0]}"
    print(f"Game over! Black pawn is promoted to a queen at {square}.")

def validator(r, c):
    return 0 <= r < N and 0 <= c < M


N, M = [int(x) for x in input().split(",")]

cheeses = 0
matrix = []
mouse = ()
for row in range(N):
    cur_row = list(input())
    if "M" in cur_row:
        mouse = (row, cur_row.index("M"))
        cur_row[mouse[1]] = "*"
    if "C" in cur_row:
        cheeses += cur_row.count("C")
    matrix.append(cur_row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

cur_m_row, cur_m_col = mouse[0], mouse[1]
while mouse:
    move = input()
    if move == "danger":
        print("Mouse will come back later!")
        matrix[mouse[0]][mouse[1]] = "M"
        break
    cur_m_row, cur_m_col = directions[move][0] + mouse[0], directions[move][1] + mouse[1]
    if not validator(cur_m_row, cur_m_col):
        print("No more cheese for tonight!")
        matrix[mouse[0]][mouse[1]] = "M"
        break
    elif matrix[cur_m_row][cur_m_col] == "C":
        matrix[cur_m_row][cur_m_col] = "*"
        cheeses -= 1
        mouse = (cur_m_row, cur_m_col)
        if not cheeses:
            matrix[mouse[0]][mouse[1]] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[cur_m_row][cur_m_col] == "@":
        continue
    elif matrix[cur_m_row][cur_m_col] == "T":
        print("Mouse is trapped!")
        mouse = (cur_m_row, cur_m_col)
        matrix[mouse[0]][mouse[1]] = "M"
        break
    elif matrix[cur_m_row][cur_m_col] == "*":
        mouse = (cur_m_row, cur_m_col)

for rows in matrix:
    print("".join(rows))

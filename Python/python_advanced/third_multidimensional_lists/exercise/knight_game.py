def validator(a, b):
    return 0 <= a < N and 0 <= b < N


N = int(input())

board = [list(input()) for _ in range(N)]

directions = [
    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1],
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2]
]

killed = 0
while True:
    mvp = []
    mvp_score = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] == "K":
                cur_kills = 0
                for d in directions:
                    if validator(r + d[0], c + d[1]):
                        if board[r + d[0]][c + d[1]] == "K":
                            cur_kills += 1

                if cur_kills > mvp_score:
                    mvp_score = cur_kills
                    mvp = [r, c]

    if mvp:
        board[mvp[0]][mvp[1]] = "0"
        killed += 1
    else:
        print(killed)
        break

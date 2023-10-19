rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    intake = input().split()
    if intake[0] == "END":
        [print(*row) for row in matrix]
        break

    command, r, c, value = intake[0], int(intake[1]), int(intake[2]), int(intake[3])

    if 0 <= r < rows and 0 <= c < len(matrix[r]):
        if command == "Add":
            matrix[r][c] += value
        else:
            matrix[r][c] -= value
    else:
        print("Invalid coordinates")

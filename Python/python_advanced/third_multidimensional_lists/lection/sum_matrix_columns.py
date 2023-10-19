rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sums = []
for col in range(cols):
    cur_sum = 0
    for row in range(rows):
        cur_sum += matrix[row][col]
    print(cur_sum)

rows, cols = [int(x) for x in input().split(", ")]

total_sum = 0
matrix = []
for _ in range(rows):
    cur_line = [int(x) for x in input().split(", ")]
    total_sum += sum(cur_line)
    matrix.append(cur_line)

print(total_sum)
print(matrix)

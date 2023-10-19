rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

largest = float("-inf")
largest_loc = []
for row in range(rows - 1):
    for col in range(cols - 1):
        result = matrix[row][col] + matrix[row + 1][col] + matrix[row][col + 1] + matrix[row + 1][col + 1]
        if result > largest:
            largest = result
            largest_loc = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

for r in range(2):
    print(*largest_loc[r], sep=" ")
print(largest)

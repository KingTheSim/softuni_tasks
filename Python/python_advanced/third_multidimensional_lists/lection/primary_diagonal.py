SIZE = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(SIZE)]

result = 0
for row in range(SIZE):
    result += matrix[row][row]

print(result)

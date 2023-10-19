SIZE = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(SIZE)]

primes = []
secundus = []
for row in range(SIZE):
    primes.append(matrix[row][row])
    secundus.append(matrix[row][SIZE - row - 1])

print(abs(sum(primes) - sum(secundus)))

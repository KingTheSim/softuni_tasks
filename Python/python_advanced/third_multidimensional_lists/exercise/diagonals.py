SIZE = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(SIZE)]

primes = []
secundus = []
for row in range(SIZE):
    primes.append(matrix[row][row])
    secundus.append(matrix[row][SIZE - row - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primes)}. Sum: {sum(primes)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secundus)}. Sum: {sum(secundus)}")

numbers = [int(x) for x in input().split()]

result = []
for i in range(len(numbers)):
    result.append(-numbers[i])

print(result)

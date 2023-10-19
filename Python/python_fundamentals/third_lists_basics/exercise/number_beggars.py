numbers = [int(x) for x in input().split(", ")]
beggars = int(input())

result = [0] * beggars
for i in range(len(numbers)):
    beggars_ind = i % beggars
    result[beggars_ind] += numbers[i]

print(result)

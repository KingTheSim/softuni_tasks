factor = int(input())
count = int(input())

result = []
counter = factor
for _ in range(count):
    result.append(counter)
    counter += factor

print(result)

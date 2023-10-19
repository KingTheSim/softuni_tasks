n = int(input())
added = 0

for i in range(n):
    number = int(input())
    added += number
average = added / n

print(f"{average:.2f}")

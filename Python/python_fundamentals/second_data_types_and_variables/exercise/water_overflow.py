n = int(input())

capacity = 255
filled = 0

for _ in range(n):
    water = int(input())
    if filled + water > capacity:
        print("Insufficient capacity!")
        continue
    else:
        filled += water

print(filled)

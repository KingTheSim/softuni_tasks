n = int(input())

even = []
odd = []
negative = []
positive = []

for _ in range(n):
    current = int(input())

    if current % 2 == 0:
        even.append(current)
    else:
        odd.append(current)

    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)

command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
else:
    print(positive)

reservations = set()

for _ in range(int(input())):
    reservations.add(input())

while True:
    command = input()

    if command == "END":
        break
    else:
        if command in reservations:
            reservations.remove(command)

reservations = list(reservations)
reservations.sort()

print(len(reservations))
for reservation in reservations:
    print(reservation)

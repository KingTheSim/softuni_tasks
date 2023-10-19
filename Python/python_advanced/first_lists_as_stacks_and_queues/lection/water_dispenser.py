from collections import deque

water_left = int(input())
people_left = deque()

while True:
    command_start = input()
    if command_start == "Start":
        break

    else:
        people_left.append(command_start)

while True:
    command = input().split()

    if len(command) == 2:
        water_left += int(command[1])

    elif command[0] == "End":
        print(f"{water_left} liters left")
        break

    else:
        needed = int(command[0])

        if water_left >= needed:
            water_left -= needed
            print(f"{people_left.popleft()} got water")

        else:
            print(f"{people_left.popleft()} must wait")

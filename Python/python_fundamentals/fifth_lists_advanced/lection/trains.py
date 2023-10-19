wagons = int(input())

train = [0] * wagons

while True:
    current = input()
    if current == "End":
        break
    command = current.split()
    if command[0] == "add":
        people = int(command[1])
        train[-1] += people
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    else:
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

print(train)

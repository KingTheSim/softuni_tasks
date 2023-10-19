gifts = input().split()

while True:
    line = input()
    if line == "No Money":
        break

    command = line.split()
    if command[0] == "OutOfStock":
        while command[1] in gifts:
            ind = gifts.index(command[1])
            gifts[ind] = None
    elif command[0] == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]
    else:
        gifts[-1] = command[1]

result = []
for i in gifts:
    if i is not None:
        print(i, end=" ")

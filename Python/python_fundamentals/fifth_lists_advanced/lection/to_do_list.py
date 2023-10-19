result = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    current = command.split("-")
    index = current[0]
    result[int(index) - 1] = current[1]

print([x for x in result if x != 0])

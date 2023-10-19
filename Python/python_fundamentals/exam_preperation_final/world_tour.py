def is_valid(text, ind):
    return 0 <= ind < len(text)


stops = input()

while True:
    commands = input().split(":")
    if commands[0] == "Travel":
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    elif commands[0] == "Add Stop":
        if is_valid(stops, int(commands[1])):
            stops = stops[:int(commands[1])] + commands[2] + stops[int(commands[1]):]
        print(stops)

    elif commands[0] == "Remove Stop":
        if is_valid(stops, int(commands[1])) and is_valid(stops, int(commands[2])):
            stops = stops[:int(commands[1])] + stops[int(commands[2]) + 1:]
        print(stops)

    else:
        if commands[1] in stops:
            stops = stops.replace(commands[1], commands[2])
        print(stops)

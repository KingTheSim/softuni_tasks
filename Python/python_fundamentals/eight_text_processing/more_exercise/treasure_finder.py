keys = [int(x) for x in input().split()]

while True:
    message = input()
    if message == "find":
        break

    index = 0
    new_message = ""
    for ch in message:
        if index == len(keys):
            index = 0
        new_message += chr(ord(ch) - keys[index])
        index += 1

    treasure = ""
    location = ""
    treasured = False
    located = False
    for ch_new in new_message:
        if ch_new == "&" and treasured:
            treasured = False
        elif ch_new == "&":
            treasured = True
        elif treasured:
            treasure += ch_new
        elif ch_new == "<":
            located = True
        elif ch_new == ">" and located:
            located = False
        elif located:
            location += ch_new

    print(f"Found {treasure} at {location}")

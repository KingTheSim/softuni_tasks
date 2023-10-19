start_list = input().split("!")

new_list = start_list
while True:
    command = input()
    if command == "Go Shopping!":
        break
    current = command.split()

    if current[0] == "Urgent":
        if current[1] in new_list:
            continue
        new_list.insert(0, current[1])

    elif current[0] == "Unnecessary":
        if current[1] not in new_list:
            continue
        new_list.remove(current[1])

    elif current[0] == "Correct":
        if current[1] not in new_list:
            continue
        item_index = new_list.index(current[1])
        new_list[item_index] = current[2]

    else:
        if current[1] not in new_list:
            continue
        new_list.remove(current[1])
        new_list.append(current[1])

print(", ".join(new_list))

def validator(num, sequence):
    return 0 <= num < len(sequence)


start = input().split()

failed = False
new_list = start
moves = 0
while True:
    command = input()
    if command == "end":
        failed = True
        break
    moves += 1
    current = [int(x) for x in command.split()]
    if validator(current[0], new_list) and validator(current[1], new_list) and not current[0] == current[1]:
        if new_list[current[0]] == new_list[current[1]]:
            print(f"Congrats! You have found matching elements - {new_list[current[0]]}!")

            if current[0] > current[1]:
                new_list.pop(current[0])
                new_list.pop(current[1])
            else:
                new_list.pop(current[1])
                new_list.pop(current[0])

        else:
            print("Try again!")
    else:
        target = len(new_list) // 2
        for i in range(2):
            new_list.insert(target, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")

    if not new_list:
        break

if failed:
    print("Sorry you lose :(")
    print(" ".join(new_list))
else:
    print(f"You have won in {moves} turns!")

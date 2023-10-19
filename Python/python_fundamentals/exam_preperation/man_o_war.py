def validator(index, ship):
    return 0 <= index < len(ship)


pirates = [int(x) for x in input().split(">")]
militia = [int(y) for y in input().split(">")]
max_health = int(input())

new_pirates = pirates
new_militia = militia
defeat = False
while not defeat:
    command = input()
    if command == "Retire":
        break
    current = command.split()

    if current[0] == "Fire":
        cur_index = int(current[1])
        if validator(cur_index, new_militia):
            damage = int(current[2])
            new_militia[cur_index] -= damage
            if new_militia[cur_index] <= 0:
                print("You won! The enemy ship has sunken.")
                defeat = True

    elif current[0] == "Defend":
        start = int(current[1])
        finish = int(current[2])
        if validator(start, new_pirates) and validator(finish, new_pirates):
            damage = int(current[3])
            for i in range(start, finish + 1):
                new_pirates[i] -= damage
                if new_pirates[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    defeat = True
                    break

    elif current[0] == "Repair":
        rep_index = int(current[1])
        if validator(rep_index, new_pirates):
            repaired = int(current[2])
            if repaired + new_pirates[rep_index] > max_health:
                new_pirates[rep_index] = max_health
            else:
                new_pirates[rep_index] += repaired

    else:
        needing_rep = max_health * 0.2
        count = 0
        for a in new_pirates:
            if a < needing_rep:
                count += 1
        print(f"{count} sections need repair.")

if not defeat:
    total_pirates = 0
    for b in new_pirates:
        total_pirates += b
    total_militia = 0
    for c in new_militia:
        total_militia += c

    print(f"Pirate ship status: {total_pirates}")
    print(f"Warship status: {total_militia}")
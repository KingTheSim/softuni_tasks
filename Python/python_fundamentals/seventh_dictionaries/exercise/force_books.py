sides = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")
        if side not in sides:
            sides[side] = []
        if [user] not in sides.values():
            sides[side].append(user)

    elif " -> " in command:
        user, side = command.split(" -> ")
        if side not in sides:
            sides[side] = []
        if [user] not in sides.values():
            sides[side].append(user)
        else:
            for cur_side, users in sides.items():
                if user in users:
                    sides[cur_side].remove(user)
                    sides[side].append(user)
        print(f"{user} joins the {side} side!")

for side, users in sides.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")

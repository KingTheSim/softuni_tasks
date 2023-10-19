number = int(input())

party = {}
for _ in range(number):
    current = input().split()
    party[current[0]] = {}
    party[current[0]]["HP"] = int(current[1])
    party[current[0]]["MP"] = int(current[2])

HP_MAX = 100
MP_MAX = 200
while True:
    command = input().split(" - ")

    if command[0] == "End":
        break

    elif command[0] == "CastSpell":
        req_mana = int(command[2])
        if party[command[1]]["MP"] >= req_mana:
            party[command[1]]["MP"] -= req_mana
            print(f"{command[1]} has successfully cast {command[3]} and now has {party[command[1]]['MP']} MP!")
        else:
            print(f"{command[1]} does not have enough MP to cast {command[3]}!")

    elif command[0] == "TakeDamage":
        damage = int(command[2])
        party[command[1]]["HP"] -= damage
        if party[command[1]]["HP"] > 0:
            print(f"{command[1]} was hit for {damage} HP"
                  f" by {command[3]} and now has {party[command[1]]['HP']} HP left!")
        else:
            print(f"{command[1]} has been killed by {command[3]}!")
            del party[command[1]]

    elif command[0] == "Recharge":
        amount = int(command[2])
        recharged = 0
        if party[command[1]]["MP"] + amount > MP_MAX:
            recharged = MP_MAX - party[command[1]]["MP"]
            party[command[1]]["MP"] = MP_MAX
        else:
            recharged = amount
            party[command[1]]["MP"] += recharged
        print(f"{command[1]} recharged for {recharged} MP!")

    else:
        healing = int(command[2])
        healed = 0
        if party[command[1]]["HP"] + healing > HP_MAX:
            healed = HP_MAX - party[command[1]]["HP"]
            party[command[1]]["HP"] = HP_MAX
        else:
            healed = healing
            party[command[1]]["HP"] += healed
        print(f"{command[1]} healed for {healed} HP!")

for hero in party:
    print(hero)
    print(f"  HP: {party[hero]['HP']}")
    print(f"  MP: {party[hero]['MP']}")

MAX_HEALTH = 100

rooms = input().split("|")

cash = 0
health = MAX_HEALTH
counter = 0
dead = False
for room in rooms:
    counter += 1
    current = room.split()

    if current[0] == "potion":
        healing = int(current[1])
        if health + healing > MAX_HEALTH:
            dif = MAX_HEALTH - health
            print(f"You healed for {dif} hp.")
            health = MAX_HEALTH
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {healing} hp.")
            health += healing
            print(f"Current health: {health} hp.")

    elif current[0] == "chest":
        money = int(current[1])
        print(f"You found {money} bitcoins.")
        cash += money

    else:
        damage = int(current[1])
        health -= damage
        monster = current[0]
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            dead = True
            break

if dead:
    print(f"Best room: {counter}")
else:
    print("You've made it!")
    print(f"Bitcoins: {cash}")
    print(f"Health: {health}")

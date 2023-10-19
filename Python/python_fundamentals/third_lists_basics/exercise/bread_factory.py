# Known
start_energy = 100
start_coins = 100

# Input
events = input().split("|")

# Logic
energy = start_energy
coins = start_coins
failed = False
for event in events:
    current = event.split("-")
    value = int(current[1])

    if current[0] == "rest":
        if energy + value > start_energy:
            print(f"You gained {start_energy - energy} energy.")
            energy = start_energy
        else:
            energy += value
            print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")

    elif current[0] == "order":
        if energy - 30 < 0:
            print("You had to rest!")
            energy += 50
        else:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")

    else:
        if coins - value >= 0:
            coins -= value
            print(f"You bought {current[0]}.")
        else:
            print(f"Closed! Cannot afford {current[0]}.")
            failed = True
            break

if not failed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

number = int(input())

favourites = {}
for _ in range(number):
    current = input().split("|")
    favourites[current[0]] = {"composer": current[1], "key": current[2]}

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break

    elif command[0] == "Add":
        if command[1] in favourites:
            print(f"{command[1]} is already in the collection!")
        else:
            favourites[command[1]] = {"composer": command[2], "key": command[3]}
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")

    elif command[0] == "Remove":
        if command[1] in favourites:
            del favourites[command[1]]
            print(f"Successfully removed {command[1]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

    else:
        if command[1] in favourites:
            favourites[command[1]]["key"] = command[2]
            print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

for key, value in favourites.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")

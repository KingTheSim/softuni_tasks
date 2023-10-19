animals = input().split(", ")

animals.reverse()
found = False
counter = 0
for a in animals:
    if a == "wolf":
        found = True
    if found:
        if counter == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
        break
    counter += 1

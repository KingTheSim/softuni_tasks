coffees = 0
reached = False
while True:
    line = input()
    if line == "END":
        break
    elif line in ["coding", "dog", "cat", "movie"]:
        coffees += 1
    elif line in ["CODING", "DOG", "CAT", "MOVIE"]:
        coffees += 2
    else:
        continue

    if coffees > 5:
        reached = True

if reached:
    print("You need extra sleep")
else:
    print(coffees)

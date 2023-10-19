collected = 0
while True:
    destination = input()
    if destination == "End":
        break
    target = float(input())
    collected = 0
    while collected < target:
        current = float(input())
        collected += current
    else:
        print(f"Going to {destination}!")

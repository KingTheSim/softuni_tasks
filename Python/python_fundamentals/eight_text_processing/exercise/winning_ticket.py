number = int(input())

for _ in range(number):
    text = input().split()
    name = ""
    age = ""
    name_start = False
    age_start = False

    for word in text:
        for ch in word:
            if ch == "@":
                name_start = True
            elif name_start and ch == "|":
                name_start = False
            elif name_start:
                name += ch
            elif ch == "#":
                age_start = True
            elif age_start and ch == "*":
                age_start = False
            elif age_start:
                age += ch

    print(f"{name} is {age} years old.")

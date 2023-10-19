start = input().split(" | ")

words = {}
for st in start:
    current = st.split(": ")
    if current[0] not in words:
        words[current[0]] = []
    words[current[0]].append(current[1])

targets = input().split(" | ")
teacher = input()

if teacher == "Hand Over":
    print(" ".join(words.keys()))
else:
    for target in targets:
        if target in words:
            print(f"{target}:")
            for value in words[target]:
                print(f" -{value}")

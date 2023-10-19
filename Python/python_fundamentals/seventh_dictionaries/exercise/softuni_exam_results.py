users = {}

while True:
    command = input()

    if command == "exam finished":
        break
    current = command.split("-")

    if current[0] not in users:
        users[current[0]] = {"banned": False}

    if current[1] == "banned":
        users[current[0]]["banned"] = True
    else:
        if not users[current[0]].get(current[1]):
            users[current[0]][current[1]] = []
        users[current[0]][current[1]].append(int(current[2]))

print("Results:")
languages = {}
for user in users:
    maximum = [0]
    if not users[user]["banned"]:
        del users[user]["banned"]
        for lang, results in users[user].items():
            if lang not in languages:
                languages[lang] = 0
            languages[lang] += len(results)
            maximum = max(maximum, results)
        print(f"{user} | {maximum[0]}")
    else:
        del users[user]["banned"]
        for lang,number in users[user].items():
            if lang not in languages:
                languages[lang] = 0
            languages[lang] += len(results)

print("Submissions:")
for key, number in languages.items():
    print(f"{key} - {number}")

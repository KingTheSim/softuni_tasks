cont_passw = {}

while True:
    command = input()
    if command == "end of contests":
        break

    cont, passw = command.split(":")
    cont_passw[cont] = passw

submissions = {}
while True:
    current = input()
    if current == "end of submissions":
        break

    contest, password, user, points = current.split("=>")
    points = int(points)
    if contest in cont_passw:
        if password == cont_passw[contest]:
            if user not in submissions:
                submissions[user] = {}
            if contest not in submissions[user]:
                submissions[user][contest] = points
            elif points >= submissions[user][contest]:
                submissions[user][contest] = points

best = ""
points = 0
for key in submissions:
    total = 0
    for value in submissions[key].values():
        total += value
    if total > points:
        best = key
        points = total
print(f"Best candidate is {best} with total {points} points.")

print("Ranking:")
for key in sorted(submissions):
    print(key)
    cur_dict = submissions[key].copy()
    for second_key, second_value in sorted(cur_dict.items(), key=lambda x: (-x[1], x[0])):
        print(f"#  {second_key} -> {second_value}")

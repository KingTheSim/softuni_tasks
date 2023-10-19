courses = {}
while True:
    command = input()
    if command == "end":
        break

    course, name = command.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(name)

for course, names in courses.items():
    print(f"{course}: {len(courses[course])}")
    for name in names:
        print(f"-- {name}")

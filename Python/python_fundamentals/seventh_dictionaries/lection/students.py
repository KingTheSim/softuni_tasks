courses = {}

current = input()
while ":" in current:
    name, id_stud, course = current.split(":")

    if course not in courses:
        courses[course] = {id_stud: name}
    else:
        courses[course][id_stud] = name
    current = input()

needed = current.replace("_", " ")
for curr_id, curr_name in courses[needed].items():
    print(f"{curr_name} - {curr_id}")

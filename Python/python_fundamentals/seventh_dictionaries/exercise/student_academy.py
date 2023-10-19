number = int(input())

students = {}
for _ in range(number):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for stud,grades in students.items():
    average = sum(grades) / len(grades)
    if average >= 4.5:
        print(f"{stud} -> {(sum(grades) / len(grades)):.2f}")

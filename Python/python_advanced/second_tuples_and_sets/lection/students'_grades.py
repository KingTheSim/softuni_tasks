record = {}

for _ in range(int(input())):
    student, grade = input().split()
    if student not in record:
        record[student] = []
    record[student].append(float(grade))

for stud, grades in record.items():
    aver = sum(grades) / len(grades)
    print(f"{stud} -> {' '.join([str(f'{x:.2f}') for x in grades])} (avg: {aver:.2f})")

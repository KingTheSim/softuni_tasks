from math import ceil
students_num = int(input())
lectures_num = int(input())
bonus_num = int(input())

maximum = 0
for i in range(students_num):
    current = int(input())
    maximum = max(maximum, current)

total_bonus = 0
if lectures_num != 0:
    total_bonus = maximum / lectures_num * (5 + bonus_num)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {maximum} lectures.")

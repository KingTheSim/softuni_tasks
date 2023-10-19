# user input
n = int(input())

# logic
total = 0
fail = 0
average = 0
good = 0
excellent = 0
for i in range(n):
    grade = float(input())
    total += grade
    if grade < 3:
        fail += 1
    elif grade < 4:
        average += 1
    elif grade < 5:
        good += 1
    else:
        excellent += 1

grades_av = total / n
perc_excellent = excellent / n * 100
perc_good = good / n * 100
perc_average = average / n * 100
perc_fail = fail / n * 100

# code output
print(f"Top students: {perc_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {perc_good:.2f}%")
print(f"Between 3.00 and 3.99: {perc_average:.2f}%")
print(f"Fail: {perc_fail:.2f}%")
print(f"Average: {grades_av:.2f}")

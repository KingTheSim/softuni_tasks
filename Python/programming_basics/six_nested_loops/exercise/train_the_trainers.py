jury = int(input())
sum_grades = 0
counter = 0

while True:
    name = input()
    current = 0
    if name == "Finish":
        break
    for i in range(jury):
        grade = float(input())
        current += grade
        sum_grades += grade
        counter += 1
    average = current / jury
    print(f"{name} - {average:.2f}.")

sum_average = sum_grades / counter
print(f"Student's final assessment is {sum_average:.2f}.")

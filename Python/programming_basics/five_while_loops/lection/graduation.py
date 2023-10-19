name = input()
year = 0
total = 0
failed_years = 0
while True:
    year += 1
    grade = float(input())
    if grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {year} grade")
            break
        year -= 1
    else:
        total += grade

    if year == 12:
        average = total / 12
        print(f"{name} graduated. Average grade: {average:.2f}")
        break

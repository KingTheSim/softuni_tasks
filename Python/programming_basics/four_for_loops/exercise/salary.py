# user input
n = int(input())
salary = float(input())

# logic
remaining_salary = salary
for i in range(n):
    tab = input()
    if tab == "Facebook":
        remaining_salary -= 150
    elif tab == "Instagram":
        remaining_salary -= 100
    elif tab == "Reddit":
        remaining_salary -= 50

    if remaining_salary <= 0:
        break

# code output
if remaining_salary > 0:
    print(int(remaining_salary))
else:
    print("You have lost your salary.")

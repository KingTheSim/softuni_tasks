def salary_finder(current_sal, structure, all_salaries):
    if all_salaries[current_sal] != 0:
        return all_salaries[current_sal]
    currently = 0
    for lower in structure[current_sal]:
        currently += salary_finder(lower, structure, all_salaries)
    if currently == 0:
        currently = 1
        all_salaries[current_sal] = currently
    else:
        all_salaries[current_sal] = currently
    return currently


n = int(input())

hierarchy = {}
salaries = {}
for i in range(n):
    current = list(input())
    hierarchy[i] = []
    salaries[i] = 0
    for ind, el in enumerate(current):
        if el == "Y":
            hierarchy[i].append(ind)

for salary in salaries:
    if salaries[salary] == 0:
        salary_finder(salary, hierarchy, salaries)

total = 0
for individual, money in salaries.items():
    total += money
print(total)

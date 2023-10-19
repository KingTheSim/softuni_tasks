student = 0
standard = 0
kid = 0
total = 0

while True:
    name = input()
    if name == "Finish":
        break
    capacity = int(input())
    current_taken = 0
    for i in range(capacity):
        ticket = input()
        if ticket == "End":
            break
        elif ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        else:
            kid += 1
        total += 1
        current_taken += 1
    taken_capacity = current_taken / capacity * 100
    print(f"{name} - {taken_capacity:.2f}% full.")

student_percent = student / total * 100
standard_percent = standard / total * 100
kid_percent = kid / total * 100

print(f"Total tickets: {total}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")

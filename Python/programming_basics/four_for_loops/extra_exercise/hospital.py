# user input
n = int(input())

# logic
doctors = 7
treated = 0
untreated = 0
current_untreated = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        if treated < untreated:
            doctors += 1
    patients = int(input())
    if patients < doctors:
        treated += patients
    else:
        current_untreated = patients - doctors
        untreated += current_untreated
        treated += patients - current_untreated

# code output
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")

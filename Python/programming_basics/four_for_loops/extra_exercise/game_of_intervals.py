# user interval
n = int(input())

# logic
points = 0
nine = 0
nineth = 0
twent_nine = 0
thir_nine = 0
fifty = 0
invalid = 0
for i in range(n):
    number = int(input())
    if 0 <= number <= 9:
        points += number * 0.2
        nine += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        nineth += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        twent_nine += 1
    elif 30 <= number <= 39:
        points += 50
        thir_nine += 1
    elif 40 <= number <= 50:
        points += 100
        fifty += 1
    else:
        points = points / 2
        invalid += 1

perc_9 = nine / n * 100
perc_19 = nineth / n * 100
perc_29 = twent_nine / n * 100
perc_39 = thir_nine / n * 100
perc_50 = fifty / n * 100
perc_inv = invalid / n * 100

# code output
print(f"{points:.2f}")
print(f"From 0 to 9: {perc_9:.2f}%")
print(f"From 10 to 19: {perc_19:.2f}%")
print(f"From 20 to 29: {perc_29:.2f}%")
print(f"From 30 to 39: {perc_39:.2f}%")
print(f"From 40 to 50: {perc_50:.2f}%")
print(f"Invalid numbers: {perc_inv:.2f}%")

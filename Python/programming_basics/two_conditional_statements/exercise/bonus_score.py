# user input
score = int(input())
bonus = 0

# logic
if score > 1000:
    bonus += score * 0.1
elif score > 100:
    bonus += score * 0.2
else:
    bonus += 5
if score % 2 == 0:
    bonus += 1
elif score % 10 == 5:
    bonus += 2
# code output
print(bonus)
print(score + bonus)

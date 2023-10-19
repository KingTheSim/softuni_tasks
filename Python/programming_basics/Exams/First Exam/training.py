import math

days = int(input())
first_day = float(input())

last_day = first_day
total = first_day
done = False
for i in range(1, days + 1):
    perc = int(input())
    last_day += last_day * perc / 100
    total += last_day
    if total >= 1000:
        done = True
        break

diff = abs(total - 1000)

if done:
    print(f"You've done a great job running {math.ceil(diff)} more   kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")

days = int(input())
daily_gain = int(input())
target = int(input())

total = 0
for i in range(1, days + 1):
    total += daily_gain

    if i % 3 == 0:
        total += daily_gain * 0.5

    if i % 5 == 0:
        total = total * 0.7

if total >= target:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    percentage = total / target * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")

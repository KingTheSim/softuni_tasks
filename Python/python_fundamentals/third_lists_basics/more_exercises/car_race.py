time = [int(x) for x in input().split()]

half = len(time) // 2
finish = half + 1

left = 0
right = 0
for i in range(half):
    current = int(time[i])
    left += current
    if current == 0:
        left = left * 0.80

reversed(time)

for i in range(half):
    current = int(time[i])
    right += current
    if current == 0:
        right = left * 0.80

if left > right:
    print(f"The winner is right with total time: {right:.1f}")
else:
    print(f"The winner is left with total time: {left:.1f}")
number = int(input())

weigh_highest = 0
time_highest = 0
quality_highest = 0
highest = float("-inf")
for _ in range(number):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality
    if value > highest:
        highest = value
        weigh_highest = weight
        time_highest = time
        quality_highest = quality

print(f"{weigh_highest} : {time_highest} = {int(highest)} ({quality_highest})")

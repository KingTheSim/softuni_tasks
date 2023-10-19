# input
lenght = int(input())
width = int(input())
height = int(input())
accessories_percent = float(input())

# logic
volume_cm = lenght * width * height
volume_lt = volume_cm / 1000
accessories_volume = volume_lt * (accessories_percent / 100)
needed_water = volume_lt - accessories_volume

# output
print(needed_water)
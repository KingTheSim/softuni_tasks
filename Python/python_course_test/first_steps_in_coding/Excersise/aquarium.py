lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_taken = float(input())

aquarium_volume = lenght_cm * width_cm * height_cm
aquarium_lt = aquarium_volume * 0.001
taken_volume = aquarium_lt * (percent_taken / 100)
needed_water = aquarium_lt - taken_volume

print(needed_water)
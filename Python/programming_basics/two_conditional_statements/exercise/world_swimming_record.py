from math import floor

# user input
current_record = float(input())
meters_to_swim = float(input())
seconds_per_meter = float(input())

# logic
extra_seconds = floor(meters_to_swim / 15) * 12.5
speed = (meters_to_swim * seconds_per_meter) + extra_seconds

# code output
if speed < current_record:
    print(f"Yes, he succeeded! The new world record is {speed:.2f} seconds.")
else:
    print(f"No, he failed! He was {speed - current_record:.2f} seconds slower.")

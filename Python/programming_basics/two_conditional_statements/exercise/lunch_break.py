from math import ceil

# user input
series_name = input()
episode_minutes = int(input())
break_minutes = int(input())

# logic
lunch_minutes = break_minutes / 8
relaxing_minutes = break_minutes / 4
remaining_minutes = break_minutes - lunch_minutes - relaxing_minutes

# code output
if remaining_minutes >= episode_minutes:
    print(f"You have enough time to watch {series_name} "
          f"and left with {ceil(remaining_minutes - episode_minutes)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, "
          f"you need {ceil(episode_minutes - remaining_minutes)} more minutes.")

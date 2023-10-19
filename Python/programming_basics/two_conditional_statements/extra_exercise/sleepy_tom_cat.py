# known
yearly_play_norm_min = 30000
workday_play_min = 63
freeday_play_min = 127
year_days = 365

# user input
freedays_number = int(input())

# logic
workdays_number = year_days - freedays_number
playtime = (freedays_number * freeday_play_min) + (workdays_number * workday_play_min)

# code output
if playtime > yearly_play_norm_min:
    print("Tom will run away")
    print(f"{(playtime - yearly_play_norm_min) // 60} hours "
          f"and {(playtime - yearly_play_norm_min) % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{(yearly_play_norm_min - playtime) // 60} hours "
          f"and {(yearly_play_norm_min - playtime) % 60} minutes less for play")

# known
t_tax = 0.7
t_day_price = 0.79
t_night_price = 0.90
b_price = 0.09 # can be used only for distance of min 20 km
tr_price = 0.06 # can be used only for distance of min 100 km
price = 0

# user input
n = int(input()) # km to travel
time = input() # can be either "day" or "night"

# logic
if n >= 100:
    price = tr_price * n
elif n >= 20:
    price = b_price * n
else:
    if time == "day":
        price = (t_day_price * n) + t_tax
    else:
        price = (t_night_price * n) + t_tax

# code output
print(f"{price:.2f}")

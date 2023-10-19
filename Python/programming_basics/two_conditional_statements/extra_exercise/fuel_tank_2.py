# known
b_price = 2.22
d_price = 2.33
g_price = 0.93
total = 0

# user input
fuel_type = input()
fuel_volume = float(input())
card = input()

# logic
if fuel_type == "Gasoline":
    if card == "Yes":
        total = fuel_volume * (b_price - 0.18)
    else:
        total = fuel_volume * b_price
elif fuel_type == "Diesel":
    if card == "Yes":
        total = fuel_volume * (d_price - 0.12)
    else:
        total = fuel_volume * d_price
else:  # gas
    if card == "Yes":
        total = fuel_volume * (g_price - 0.08)
    else:
        total = fuel_volume * g_price

if 20 <= fuel_volume <= 25:
    total = total * 0.92
elif fuel_volume > 25:
    total = total * 0.90

# code output
print(f"{total:.2f} lv.")

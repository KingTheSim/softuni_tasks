kg = float(input())
courier = input()
distance = int(input())

extra = 0
price = 0
if courier == "standard":
    if kg < 1:
        price = distance * 0.03
    elif 1 <= kg < 10:
        price = distance * 0.05
    elif 10 <= kg < 40:
        price = distance * 0.1
    elif 40 <= kg < 90:
        price = distance * 0.15
    elif 90 <= kg <= 150:
        price = distance * 0.20
else:
    if kg < 1:
        extra = 0.03 * 0.8 * distance * kg
        price = (distance * 0.03) + extra
    elif 1 <= kg < 10:
        extra = 0.05 * 0.4 * distance * kg
        price = (distance * 0.05) + extra
    elif 10 <= kg < 40:
        extra = 0.1 * 0.05 * distance * kg
        price = (distance * 0.1) + extra
    elif 40 <= kg < 90:
        extra = 0.15 * 0.02 * distance * kg
        price = (distance * 0.15) + extra
    elif 90 <= kg <= 150:
        extra = 0.2 * 0.01 * distance * kg
        price = (distance * 0.20) + extra

print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price:.2f} lv.")

# user input
month = input()
nights = int(input())

# logic
price_studio = 0
price_apt = 0
if month in ["May", "October"]:
    price_studio = 50 * nights
    price_apt = 65 * nights
    if nights > 14:
        price_studio = price_studio * 0.70
        price_apt = price_apt * 0.90
    elif nights > 7:
        price_studio = price_studio * 0.95
elif month in ["June", "September"]:
    price_studio = 75.20 * nights
    price_apt = 68.70 * nights
    if nights > 14:
        price_studio = price_studio * 0.80
        price_apt = price_apt * 0.90
elif month in ["July", "August"]:
    price_studio = 76 * nights
    price_apt = 77 * nights
    if nights > 14:
        price_apt = price_apt * 0.90

# code output
print(f"Apartment: {price_apt:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")

# user input
season = input()
group_type = input()
crew = int(input())
nights = int(input())

# logic
price = 0
sport = ""

if group_type in ["boys", "girls"]:
    if season == "Winter":
        price = 9.60 * crew * nights
        if group_type == "boys":
            sport = "Judo"
        else:
            sport = "Gymnastics"
    elif season == "Spring":
        price = 7.20 * crew * nights
        if group_type == "boys":
            sport = "Tennis"
        else:
            sport = "Athletics"
    else:
        price = 15 * crew * nights
        if group_type == "boys":
            sport = "Football"
        else:
            sport = "Volleyball"
else:
    if season == "Winter":
        price = 10 * crew * nights
        sport = "Ski"
    elif season == "Spring":
        price = 9.50 * crew * nights
        sport = "Cycling"
    else:
        price = 20 * crew * nights
        sport = "Swimming"

if 10 <= crew < 20:
    price = price * 0.95
elif 20 <= crew < 50:
    price = price * 0.85
elif crew >= 50:
    price = price * 0.50

# code output
print(f"{sport} {price:.2f} lv.")

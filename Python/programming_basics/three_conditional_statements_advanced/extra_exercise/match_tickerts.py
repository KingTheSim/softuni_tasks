# known
vip = 499.99
normal = 249.99

# user input
budget = float(input())
type_ticket = input()
crew_num = int(input())

# logic
ticket_price = 0
if type_ticket == "VIP":
    ticket_price = vip * crew_num
else:
    ticket_price = normal * crew_num

trip_price = 0
if crew_num < 5:
    trip_price = budget * 0.75
elif 5 <= crew_num <= 9:
    trip_price = budget * 0.60
elif 10 <= crew_num <= 24:
    trip_price = budget * 0.50
elif 25 <= crew_num <= 49:
    trip_price = budget * 0.40
else:
    trip_price = budget * 0.25

final_price = ticket_price + trip_price
diff = abs(budget - final_price)

# code output
if budget >= final_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

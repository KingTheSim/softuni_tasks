# known
one_person = 18.00
apartment = 25.00
president_apt = 35.00

# user input
days = int(input())
room = input()
experience = input()

# logic
price = 0
if room == "room for one person":
    price = one_person * (days - 1)
elif room == "apartment":
    if days > 15:
        price = apartment * (days - 1) * 0.50
    elif 10 <= days <= 15:
        price = apartment * (days - 1) * 0.65
    else:
        price = apartment * (days - 1) * 0.70
elif room == "president apartment":
    if days > 15:
        price = president_apt * (days - 1) * 0.80
    elif 10 <= days <= 15:
        price = president_apt * (days - 1) * 0.85
    else:
        price = president_apt * (days - 1) * 0.10

if experience == "positive":
    price = price * 1.25
else:
    price = price * 0.90

# user output
print(f"{price:.2f}")

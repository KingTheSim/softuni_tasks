# user input
hr_num = int(input())
roses_num = int(input())
tulips_num = int(input())
season = input()
holiday = input()

# logic
hr_price = 0
roses_price = 0
tulips_price = 0
total = 0

if season in ["Spring", "Summer"]:
    hr_price = 2.00 * hr_num
    roses_price = 4.10 * roses_num
    tulips_price = 2.50 * tulips_num
else:
    hr_price = 3.75 * hr_num
    roses_price = 4.50 * roses_num
    tulips_price = 4.15 * tulips_num

if holiday == "Y":
    total = (hr_price + roses_price + tulips_price) * 1.15
else:
    total = hr_price + roses_price + tulips_price

if season == "Spring" and tulips_num > 7:
    total = total * 0.95

if season == "Winter" and roses_num >= 10:
    total = total * 0.90

if hr_num + roses_num + tulips_num > 20:
    total = total * 0.80

total += 2
# code output
print(f"{total:.2f}")

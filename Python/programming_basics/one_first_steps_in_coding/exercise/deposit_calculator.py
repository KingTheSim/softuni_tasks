# input
deposit = float(input())
months = int(input())
annual_percent = float(input())

# logic
percentage = annual_percent / 100
increase = deposit * percentage
per_month = increase / 12
total = deposit + (months * per_month)

# output
print(total)
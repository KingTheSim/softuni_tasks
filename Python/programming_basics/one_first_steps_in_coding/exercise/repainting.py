# input
poliester_cub_cm = int(input())
paint_lt = int(input())
solvent_lt = int(input())
completion_hours = int(input())

# logic
price_poliester = (poliester_cub_cm + 2) * 1.50
price_paint = (paint_lt * 1.1) * 14.50
price_solvent = solvent_lt * 5.00
supplies_price = price_poliester + price_paint + price_solvent + 0.40
workers_salaries = (supplies_price * 0.30) * completion_hours
total_price = supplies_price + workers_salaries

# output
print(total_price)
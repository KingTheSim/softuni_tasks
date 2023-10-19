poliester_cm = int(input())
paint_lt = int(input())
diluent_lt = int(input())
work_hours = int(input())
bags_price = 0.4

needed_poliester = poliester_cm + 2
needed_paint = paint_lt * 1.1

price_poliester = needed_poliester * 1.5
price_paint = needed_paint * 14.5
price_diluent = diluent_lt * 5

materials_price = price_poliester + price_paint + price_diluent + bags_price
workers_price = (materials_price * 0.3) * work_hours
end_sum = materials_price + workers_price
print(end_sum)

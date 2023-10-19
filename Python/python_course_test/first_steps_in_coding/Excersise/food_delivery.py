number_chichen = int(input())
number_fish = int(input())
number_veg = int(input())

chichen_price = number_chichen * 10.35
fish_price = number_fish * 12.40
veg_price = number_veg * 8.15

menu_price = chichen_price + fish_price + veg_price
dessert_price = menu_price * 0.2
total_price = menu_price + dessert_price + 2.50

print(total_price)
# input
chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

# logic
price_chicken_menus = chicken_menus * 10.35
price_fish_menus = fish_menus * 12.40
price_vegetarian_menus = vegetarian_menus * 8.15
price_for_all_menus = price_chicken_menus + price_fish_menus + price_vegetarian_menus
dessert_price = price_for_all_menus * 0.20
total = price_for_all_menus + dessert_price + 2.50

# output
print(total)
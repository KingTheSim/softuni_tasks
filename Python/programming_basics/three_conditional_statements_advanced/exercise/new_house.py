# known
price_roses = 5.00
price_dahlias = 3.80
price_tulips = 2.80
price_narcissus = 3
price_gladiolus = 2.50

# user input
type_flower = input()
flowers_num = int(input())
budget = int(input())
price_flowers = 0

# logic
if type_flower == "Roses":
    if flowers_num > 80:
        price_flowers = (price_roses * 0.90) * flowers_num
    else:
        price_flowers = price_roses * flowers_num
elif type_flower == "Dahlias":
    if flowers_num > 90:
        price_flowers = (price_dahlias * 0.85) * flowers_num
    else:
        price_flowers = price_dahlias * flowers_num
elif type_flower == "Tulips":
    if flowers_num > 80:
        price_flowers = (price_tulips * 0.85) * flowers_num
    else:
        price_flowers = price_tulips * flowers_num
elif type_flower == "Narcissus":
    if flowers_num < 120:
        price_flowers = (price_narcissus * 1.15) * flowers_num
    else:
        price_flowers = price_narcissus * flowers_num
elif type_flower == "Gladiolus":
    if flowers_num < 80:
        price_flowers = (price_gladiolus * 1.20) * flowers_num
    else:
        price_flowers = price_gladiolus * flowers_num
diff = abs(price_flowers - budget)

# code output
if price_flowers <= budget:
    print(f"Hey, you have a great garden with {flowers_num} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

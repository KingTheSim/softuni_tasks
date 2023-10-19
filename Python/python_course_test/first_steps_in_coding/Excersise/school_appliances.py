pencil_number = int(input())
markers_number = int(input())
detergent_liters = int(input())
discount_percentage = int(input())
pencil_price = pencil_number * 5.80
markers_price = markers_number * 7.20
detergent_price = detergent_liters * 1.20
total_sum = pencil_price + markers_price + detergent_price
discount_sum = total_sum * (discount_percentage / 100)
discounted_sum = total_sum - discount_sum
print(discounted_sum)
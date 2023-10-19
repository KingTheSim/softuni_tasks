# input
pen_packages = int(input())
marker_packages = int(input())
detergent_lt = int(input())
percent_discount = int(input())

# logic
pens_price = pen_packages * 5.80
markers_price = marker_packages * 7.20
detergent_price = detergent_lt * 1.20
price_without_discount = pens_price + markers_price + detergent_price
discount = price_without_discount * (percent_discount / 100)
final_price = price_without_discount - discount

# output
print(final_price)
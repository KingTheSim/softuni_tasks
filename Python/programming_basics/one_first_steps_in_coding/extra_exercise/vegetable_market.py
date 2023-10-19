# input
vegetables_price_per_kg_bgn = float(input())
fruits_price_per_kg_bgn = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

# logic
total_vegetables_price_bgn = vegetables_price_per_kg_bgn * kg_vegetables
total_fruits_price_bgn = fruits_price_per_kg_bgn * kg_fruits
combined_price_eur = (total_vegetables_price_bgn + total_fruits_price_bgn) / 1.94

# output
print('{:.2f}'.format(combined_price_eur))

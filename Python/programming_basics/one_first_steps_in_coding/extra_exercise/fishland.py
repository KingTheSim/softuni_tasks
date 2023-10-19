# input
price_scumria = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_mussels = float(input())

# logic
palamud_price = price_scumria * 1.6
safrid_price = price_caca * 1.8

total_for_palamud = kg_palamud * palamud_price
total_for_safrid = kg_safrid * safrid_price
total_for_mussels = kg_mussels * 7.5
total_for_all = total_for_palamud + total_for_safrid + total_for_mussels

# output
print('{:.2f}'.format(total_for_all))

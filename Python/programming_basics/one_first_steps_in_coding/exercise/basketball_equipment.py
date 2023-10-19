# input
yearly_tax = int(input())

# logic
shoes_price = yearly_tax * 0.6
clothing_price = shoes_price * 0.8
ball_price = clothing_price / 4
accessories_price = ball_price / 5
total_sum = yearly_tax + shoes_price + clothing_price + ball_price + accessories_price

# output
print(total_sum)
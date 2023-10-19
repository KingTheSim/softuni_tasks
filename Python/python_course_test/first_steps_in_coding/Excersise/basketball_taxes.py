yearly_tax = int(input())

price_shoes = yearly_tax * 0.6
price_suit = price_shoes * 0.8
price_ball = price_suit / 4
price_acs = price_ball / 5
total_price = yearly_tax + price_shoes + price_suit + price_ball + price_acs
print(total_price)
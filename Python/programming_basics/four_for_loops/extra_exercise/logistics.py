# user input
n = int(input())

# logic
price = 0
whole_tons = 0
tons_bus = 0
tons_truck = 0
tons_train = 0

for i in range(n):
    tons = int(input())
    if tons <= 3:
        price += tons * 200
        whole_tons += tons
        tons_bus += tons
    elif 3 < tons <= 11:
        price += tons * 175
        whole_tons += tons
        tons_truck += tons
    else:
        price += tons * 120
        whole_tons += tons
        tons_train += tons

av_price = price / whole_tons
perc_bus = tons_bus / whole_tons * 100
perc_truck = tons_truck / whole_tons * 100
perc_train = tons_train / whole_tons * 100

# code output
print(f"{av_price:.2f}")
print(f"{perc_bus:.2f}%")
print(f"{perc_truck:.2f}%")
print(f"{perc_train:.2f}%")

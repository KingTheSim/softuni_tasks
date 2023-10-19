elements = input().split()

stock = {}
for i in range(0, len(elements), 2):
    stock[elements[i]] = int(elements[i + 1])
print(stock)

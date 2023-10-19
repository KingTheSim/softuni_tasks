elements = input().split()

stock = {}
for i in range(0, len(elements), 2):
    stock[elements[i]] = int(elements[i + 1])

searched = input().split()
for s in searched:
    if s in stock:
        print(f"We have {stock[s]} of {s} left")
    else:
        print(f"Sorry, we don't have {s}")

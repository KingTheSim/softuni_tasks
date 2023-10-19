number = int(input())

start = 97
finish = start + number

for a in range(start, finish):
    for b in range(start, finish):
        for c in range(start, finish):
            print(f"{chr(a)}{chr(b)}{chr(c)}")

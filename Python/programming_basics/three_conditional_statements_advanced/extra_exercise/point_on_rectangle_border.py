# user input
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

# logic
if x in [x1, x2]:
    if y1 <= y <= y2:
        print("Border")
    else:
        print("Inside / Outside")
elif y in [y1, y2]:
    if x1 <= x <= x2:
        print("Border")
    else:
        print("Inside / Outside")
else:
    print("Inside / Outside")

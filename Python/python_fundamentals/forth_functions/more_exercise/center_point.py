from math import floor


def finder(x1, y1, x2, y2):
    abs_first = abs(x1) + abs(y1)
    abs_second = abs(x2) + abs(y2)
    if abs_first <= abs_second:
        result = x1, y1
    else:
        result = x2, y2
    a = floor(result[0])
    b = floor(result[1])
    return a, b


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

print(finder(x_1, y_1, x_2, y_2))

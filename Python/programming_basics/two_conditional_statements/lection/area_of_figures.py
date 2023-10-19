from math import pi

# known
area = 0

# input
figure_type = input()

# logic
if figure_type == "square":
    a = float(input())
    area = a ** 2

elif figure_type == "rectangle":
    a, b = float(input()), float(input())
    area = a * b

elif figure_type == "circle":
    r = float(input())
    area = pi * r ** 2

elif figure_type == "triangle":
    a, h = float(input()), float(input())
    area = a * h / 2

# output
print(f"{area:.3f}")

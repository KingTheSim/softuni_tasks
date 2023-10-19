import math

# input
r_radius = float(input())

# logic
circle_area = math.pi * (r_radius * r_radius)
circle_parameter = 2 * math.pi * r_radius

# output
print('{:.2f}'.format(circle_area))
print('{:.2f}'.format(circle_parameter))

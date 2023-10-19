# known
green_paint_cub_m_coverage = 3.4
red_paint_cub_m_coverage = 4.3
front_door_height = 2
front_door_lenght = 1.2
cubic_window_side = 1.5

# input
x_house_height = float(input())
y_house_lenght = float(input())
h_triangle_roof_side_height = float(input())

# logic
side_area = x_house_height * y_house_lenght
window_area = cubic_window_side * cubic_window_side
combined_sides_paintable_area = (side_area * 2) - (window_area * 2)

back_side_area = x_house_height * x_house_height
front_door_area = front_door_height * front_door_lenght
combined_front_and_backside_paintable_area = (back_side_area * 2) - front_door_area

combined_non_roof_paintable_area = combined_sides_paintable_area + combined_front_and_backside_paintable_area
needed_green_paint = combined_non_roof_paintable_area / green_paint_cub_m_coverage

roof_triangle_sides_area = (x_house_height * h_triangle_roof_side_height / 2) * 2
roof_rectangle_sides_area = (x_house_height * y_house_lenght) * 2
combined_roof_paintable_area = roof_triangle_sides_area + roof_rectangle_sides_area
needed_red_paint = combined_roof_paintable_area / red_paint_cub_m_coverage

# output
print('{:.2f}'.format(needed_green_paint))
print('{:.2f}'.format(needed_red_paint))

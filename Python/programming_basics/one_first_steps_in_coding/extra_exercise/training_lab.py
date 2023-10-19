# input
lab_wenght_m = float(input())
lab_width_m = float(input())

# logic
seats_row_number = lab_wenght_m // 1.2
seats_collumn_number = (lab_width_m - 1) // 0.7
total_seats = (seats_row_number * seats_collumn_number) - 3

# output
print(int(total_seats))

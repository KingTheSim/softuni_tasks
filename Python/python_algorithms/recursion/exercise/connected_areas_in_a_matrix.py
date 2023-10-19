def spot_validator(row, col, matrix):
    if row >= len(matrix) or row < 0:
        return False
    elif col >= len(matrix[row]) or col < 0:
        return False
    elif matrix[row][col] == "*":
        return False
    elif matrix[row][col] == "v":
        return False
    else:
        return True


def area_counter(row, col,  matrix):
    if spot_validator(row, col, matrix):
        matrix[row][col] = "v"
        result = 1
        result += area_counter(row + 1, col, matrix)
        result += area_counter(row - 1, col, matrix)
        result += area_counter(row, col + 1, matrix)
        result += area_counter(row, col - 1, matrix)
        return result
    else:
        return 0


def area_finder(areas, matrix):
    for cur_row in range(len(matrix)):
        for cur_col in range(len(matrix[cur_row])):
            if spot_validator(cur_row, cur_col, matrix):
                areas[(cur_row, cur_col)] = area_counter(cur_row, cur_col, matrix)


r = int(input())
c = int(input())

mat = []
for _ in range(r):
    mat.append([x for x in input()])

areas = {}
area_finder(areas, mat)
sorted_areas = dict(sorted(areas.items(), key=lambda x: -x[1]))
print(f"Total areas found: {len(sorted_areas)}")

counter = 0
for area, count in sorted_areas.items():
    counter += 1
    print(f"Area #{counter} at {area}, size: {count}")

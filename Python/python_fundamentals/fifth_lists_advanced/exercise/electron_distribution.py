el_number = int(input())

counter = 1
layers = []
left = el_number
while left > 0:
    capacity = 2 * (counter ** 2)
    if capacity < left:
        left -= capacity
        layers.append(capacity)
    else:
        layers.append(left)
        left = 0
    counter += 1

print(layers)

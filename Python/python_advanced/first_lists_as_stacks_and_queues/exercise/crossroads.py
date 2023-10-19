from collections import deque

green_time = int(input())
window = int(input())

cars = deque()
nums_greens = 0
num_cars = 0
time = green_time

while True:
    command = input()

    if command == "END":
        break

    elif command == "green":
        nums_greens += 1
    else:
        cars.append(command)

nums_greens -= 1
while cars:
    cur_car = cars.popleft()

    if len(cur_car) <= time:
        time -= len(cur_car)
        num_cars += 1

    elif len(cur_car) <= time + window and time > 0:
        num_cars += 1
        if nums_greens != 0:
            time = green_time
            nums_greens -= 1
        else:
            time = 0

    else:
        if nums_greens == 0 and time != 0:
            print("A crash happened!")
            target = cur_car[time + window]
            print(f"{cur_car} was hit at {target}.")
            break
        elif nums_greens > 0:
            nums_greens -= 1
            time = green_time
            cars.appendleft(cur_car)


else:
    print("Everyone is safe.")
    print(f"{num_cars} total cars passed the crossroads.")
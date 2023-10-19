parking = set()

for _ in range(int(input())):
    act, car = input().split(", ")

    if act == "IN":
        parking.add(car)
    else:
        if car in parking:
            parking.remove(car)

if parking:
    print(*parking, sep="\n")
else:
    print("Parking Lot is Empty")

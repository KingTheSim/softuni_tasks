cars = input().split(">>")

total = 0
for car in cars:
    current = car.split()
    paid = 0

    if current[0] == "family":
        paid = 50
        yearly_dec = int(current[1]) * 5
        yearly_incr = (int(current[2]) // 3000) * 12
        paid = paid - yearly_dec + yearly_incr

    elif current[0] == "heavyDuty":
        paid = 80
        yearly_dec = int(current[1]) * 8
        yearly_incr = (int(current[2]) // 9000) * 14
        paid = paid - yearly_dec + yearly_incr

    elif current[0] == "sports":
        paid = 100
        yearly_dec = int(current[1]) * 9
        yearly_incr = (int(current[2]) // 2000) * 18
        paid = paid - yearly_dec + yearly_incr

    else:
        print("Invalid car type.")
        continue

    print(f"A {current[0]} car will pay {paid:.2f} euros in taxes.")
    total += paid

print(f"The National Revenue Agency will collect {total:.2f} euros in taxes.")

total = 0
while True:
    us_input = input()
    if us_input == "NoMoreMoney":
        break
    current_sum = float(us_input)
    if current_sum < 0:
        print(f"Invalid operation!")
        break
    print(f"Increase: {current_sum:.2f}")
    total += current_sum

print(f"Total: {total:.2f}")

cpu = float(input())
gpu = float(input())
RAM = float(input())
RAM_number = int(input())
discount = float(input())

cpu_discount = cpu * discount
gpu_discount = gpu * discount

RAM_price = RAM * RAM_number
cpu_price = cpu - cpu_discount
gpu_price = gpu - gpu_discount

total = RAM_price + cpu_price + gpu_price
total_leva = total * 1.57

print(f"Money needed - {total_leva:.2f} leva.")

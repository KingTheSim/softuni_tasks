# known
gpu_price = 250
# cpu price is 35% of the price for all the gpu's
# ram price is 10% of the price for all the gpu's

# user input
budget = float(input())
gpu_number = int(input())
cpu_number = int(input())
ram_number = int(input())

# logic
gpu_total_price = gpu_price * gpu_number

cpu_price = gpu_total_price * 0.35
cpu_total_price = cpu_price * cpu_number

ram_price = gpu_total_price * 0.1
ram_total_price = ram_price * ram_number

total_price = gpu_total_price + cpu_total_price + ram_total_price
if gpu_number > cpu_number:
    total_price -= total_price * 0.15

# code output
if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")

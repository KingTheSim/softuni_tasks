# user input
interval = int(input())

# logic
p_1_sum = 0
p_2_sum = 0
p_3_sum = 0
p_4_sum = 0
p_5_sum = 0

for i in range(interval):
    current_num = int(input())
    if current_num < 200:
        p_1_sum += 1
    elif 200 <= current_num <= 399:
        p_2_sum += 1
    elif 400 <= current_num <= 599:
        p_3_sum += 1
    elif 600 <= current_num <= 799:
        p_4_sum += 1
    elif current_num >= 800:
        p_5_sum += 1

p_sum = p_1_sum + p_2_sum + p_3_sum + p_4_sum + p_5_sum
perc_p_1 = p_1_sum / p_sum * 100
perc_p_2 = p_2_sum / p_sum * 100
perc_p_3 = p_3_sum / p_sum * 100
perc_p_4 = p_4_sum / p_sum * 100
perc_p_5 = p_5_sum / p_sum * 100

# code output
print(f"{perc_p_1:.2f}%")
print(f"{perc_p_2:.2f}%")
print(f"{perc_p_3:.2f}%")
print(f"{perc_p_4:.2f}%")
print(f"{perc_p_5:.2f}%")
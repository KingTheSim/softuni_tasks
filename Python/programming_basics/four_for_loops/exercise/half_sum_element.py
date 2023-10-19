from sys import maxsize

# user input
max_num = -maxsize
range_num = int(input())
total_sum = 0
for num in range(range_num):
    current_num = int(input())
    total_sum += current_num
    if current_num > max_num:
        max_num = current_num

final_sum = total_sum - max_num
diff = abs(final_sum - max_num)
if max_num == final_sum:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {diff}")

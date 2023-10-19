# user input
n = int(input())

# logic
first_num = 0
last_result = 0
max_diff = 0
count = 0
result = 0
diff = 0
difference = False
iterations_count = 0
for i in range(n * 2):
    iterations_count += 1
    number = int(input())
    if count == 0:
        count += 1
        first_num = number
    else:
        count = 0
        result = number + first_num
    if iterations_count >= 4:
        if result != last_result:
            difference = True
            diff = abs(result - last_result)
    if max_diff < diff:
        max_diff = diff
    last_result = result

# code output
if difference:
    print(f"No, maxdiff={max_diff}")
else:
    print(f"Yes, value={last_result}")

# user input
n = int(input())

# logic
result_left = 0
result_right = 0

for i in range((n * 2)):
    number = int(input())
    if i >= n:
        result_right += number
    else:
        result_left += number

diff = abs(result_right - result_left)

# code output
if result_left == result_right:
    print(f"Yes, sum = {result_right}")
else:
    print(f"No, diff = {diff}")

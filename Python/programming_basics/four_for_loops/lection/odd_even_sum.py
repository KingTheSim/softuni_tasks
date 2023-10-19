# user input
n = int(input())

# logic
result_even = 0
result_odd = 0

for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        result_even += number
    else:
        result_odd += number

diff = abs(result_even - result_odd)

# code output
if result_even == result_odd:
    print("Yes")
    print(f"Sum = {result_even}")
else:
    print("No")
    print(f"Diff = {diff}")


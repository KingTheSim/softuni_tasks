import sys

# input
n = int(input())

# logic
max_number = -sys.maxsize
min_number = sys.maxsize
number = 0

for _ in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

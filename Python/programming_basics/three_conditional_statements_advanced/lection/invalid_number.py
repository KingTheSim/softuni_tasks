# user input
number = int(input())

# logic
is_valid = 100 <= number <= 200 or number == 0
if not is_valid:
    print("invalid")

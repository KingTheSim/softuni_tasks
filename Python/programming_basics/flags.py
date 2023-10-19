# user input
n1 = int(input())
n2 = int(input())
operator = input()

# logic
result = 0
impossible_flag = False
division_flag = False
if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    division_flag = True
    if n2 == 0:
        impossible_flag = True
    else:
        result = n1 / n2
elif operator == "%":
    division_flag = True
    if n2 == 0:
        impossible_flag = True
    else:
        result = n1 % n2

# code output
if division_flag:
    if operator == "/":
        if impossible_flag:
            print(f"Cannot divide {n1} by zero")
        else:
            print(f"{n1} {operator} {n2} = {result:.2f}")
    else:
        if impossible_flag:
            print(f"Cannot divide {n1} by zero")
        else:
            print(f"{n1} {operator} {n2} = {result}")
else:
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

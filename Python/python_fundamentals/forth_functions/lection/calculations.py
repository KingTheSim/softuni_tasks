def operation(operator, n1, n2):
    if operator == "multiply":
        return n1 * n2
    elif operator == "divide":
        return int(n1 / n2)
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


operator = input()
n_1 = int(input())
n_2 = int(input())

print(operation(operator, n_1, n_2))

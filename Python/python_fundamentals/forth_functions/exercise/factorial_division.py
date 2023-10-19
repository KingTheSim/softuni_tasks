def factorer(num):
    result = 1
    for i in range(2, num + 1):
        result = result * i
    return result

first = int(input())
second = int(input())

first_factorial = factorer(first)
second_factorial = factorer(second)
total = first_factorial / second_factorial
print(f"{total:.2f}")

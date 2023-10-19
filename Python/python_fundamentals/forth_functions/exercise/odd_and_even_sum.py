def evener(num):
    return num % 2 == 0


numbers = input()
even_sum = 0
odd_sum = 0

for i in numbers:
    number = int(i)
    if evener(number):
        even_sum += number
    else:
        odd_sum += number

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

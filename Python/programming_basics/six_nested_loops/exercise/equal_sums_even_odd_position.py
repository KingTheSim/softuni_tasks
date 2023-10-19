first = int(input())
last = int(input())

for i in range(first, last + 1):
    current = str(i)
    sum_even = 0
    sum_odd = 0
    for n in range(0, len(current)):
        digit = int(current[n])

        if n % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    if sum_even == sum_odd:
        print(current, end=" ")

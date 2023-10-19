from sys import maxsize
odd_min = maxsize
odd_max = -maxsize
odd_sum = 0
last_odd = 0
odd_diff = False

even_min = maxsize
even_max = - maxsize
even_sum = 0
last_even = 0
even_diff = False

n = int(input())
for i in range(1, n + 1):
    current = float(input())
    if i % 2 != 0:
        odd_sum += current
        if i == 1:
            last_odd = current
            odd_min = current
            odd_max = current
        elif last_odd != current:
            if current > odd_max:
                odd_max = current
            if current < odd_min:
                odd_min = current
    else:
        even_sum += current
        if i == 2:
            last_even = current
            even_min = current
            even_max = current
        elif last_even != current:
            if current > even_max:
                even_max = current
            if current < even_min:
                even_min = current

print(f"OddSum={odd_sum:.2f},")
if n >= 1:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMin=No,")
    print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if n >= 2:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMin=No,")
    print("EvenMax=No")

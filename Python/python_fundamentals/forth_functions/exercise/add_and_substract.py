def adder(a, b):
    return a + b


def subtractor(a, b):
    return a - b


def calcul(a, b, c):
    return subtractor(adder(a, b), c)


first = int(input())
second = int(input())
third = int(input())

print(calcul(first, second, third))

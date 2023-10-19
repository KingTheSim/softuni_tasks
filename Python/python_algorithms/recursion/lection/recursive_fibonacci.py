def fibonaccier(number):
    if number <= 1:
        return 1
    return fibonaccier(number - 1) + fibonaccier(number - 2)


def iterer(number):
    first = 1
    second = 1
    result = 0
    for _ in range(number - 1):
        result = first + second
        first, second = second, result
    return result


n = int(input())

print(iterer(n))

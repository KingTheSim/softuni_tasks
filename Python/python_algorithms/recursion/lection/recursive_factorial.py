def factorialer(number):
    if number == 1:
        return 1
    return number * factorialer(number - 1)


target = int(input())

print(factorialer(target))

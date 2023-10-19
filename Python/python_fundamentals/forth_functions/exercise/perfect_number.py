def evener(num):
    return num % 2 == 0


def perfecter(num):
    result = 0
    target = int(num / 2)
    for i in range(1, target + 1):
        if num % i == 0:
            result += i
    return num == result


number = int(input())

if evener(number) and perfecter(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

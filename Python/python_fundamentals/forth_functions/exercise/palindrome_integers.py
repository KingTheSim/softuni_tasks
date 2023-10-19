def palindromer(num):
    return num == reverser(num)


def reverser(num):
    result = []
    for a in range(-1, -len(num) - 1, -1):
        result.append(num[a])

    return "".join(result)


numbers = input().split(", ")
for i in numbers:
    print(palindromer(i))

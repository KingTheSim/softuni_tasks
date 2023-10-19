def finder(a, b):
    between = []
    for i in range(a + 1, b):
        between.append(chr(i))
    return between


start = input()
finish = input()

result = finder(ord(start), ord(finish))
print(" ".join(result))

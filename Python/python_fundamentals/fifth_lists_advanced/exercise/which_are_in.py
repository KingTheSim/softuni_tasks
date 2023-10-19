def substringer(x, searched):
    for i in searched:
        if x in i:
            return True


substrings = input().split(", ")
strings = input().split(", ")

result = [x for x in substrings if substringer(x, strings)]
print(result)

def palindromer(text):
    return text == reverser(text)


def reverser(text):
    result = []
    for a in range(-1, -len(text) - 1, -1):
        result.append(text[a])

    return "".join(result)


line = input().split()
searched = input()

result = [x for x in line if palindromer(x)]
print(result)
print(f"Found palindrome {result.count(searched)} times")

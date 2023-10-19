text = input()

result = ""
current = ""
for char in text:
    if char != current:
        current = char
        result += char

print(result)

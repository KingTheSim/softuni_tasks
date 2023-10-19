text = input()

result = ""
strength = 0
for i in range(len(text)):
    if text[i] == ">":
        strength += int(text[i + 1])
        result += text[i]
        continue
    if strength > 0:
        strength -= 1
        continue
    result += text[i]

print(result)

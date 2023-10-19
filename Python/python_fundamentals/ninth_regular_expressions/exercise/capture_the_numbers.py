import re

pattern = r"[0-9]+"
finale = []
while True:
    text = input()
    if not text:
        break

    current = re.findall(pattern, text)
    for number in current:
        finale.append(number)

print(" ".join(finale))

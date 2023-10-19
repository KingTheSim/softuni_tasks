import re

text = input()

pattern = r"(^|(?<=\s))[A-Za-z0-9]+([\.\-\_][A-Za-z0-9]+)*@[a-zA-Z]+([\.\-][a-zA-Z]+)+($|(?=,)|(?=.))"
results = re.finditer(pattern, text)
for res in results:
    print(res.group())

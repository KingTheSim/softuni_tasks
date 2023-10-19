import re

text = input().lower()
target = input().lower()

pattern = rf"\b{target}\b"
found = re.findall(pattern, text)
print(len(found))

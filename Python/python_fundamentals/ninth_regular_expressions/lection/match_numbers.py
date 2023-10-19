import re

text = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
nums = re.finditer(pattern, text)

for num in nums:
    print(num.group(), end=" ")

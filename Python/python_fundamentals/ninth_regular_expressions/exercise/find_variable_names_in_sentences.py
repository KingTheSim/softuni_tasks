import re

text = input()

pattern = r"\b_[A-Za-z0-9]+\b"
variables = re.findall(pattern, text)
final = []
for part in variables:
    final.append(part[1:])
print(",".join(final))

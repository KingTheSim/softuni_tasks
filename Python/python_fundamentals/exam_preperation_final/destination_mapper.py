import re

destinations = input()

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, destinations)

final = []
score = 0
if matches:
    for match in matches:
        match = match.group(2)
        final.append(match)
        score += len(match)

print(f"Destinations: {', '.join(final)}")
print(f"Travel Points: {score}")

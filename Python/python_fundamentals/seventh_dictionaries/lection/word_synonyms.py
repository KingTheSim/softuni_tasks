times = int(input())

synonyms = {}
for _ in range(times):
    key = input()
    value = input()
    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(value)

for key in synonyms:
    print(f"{key} - {', '.join(synonyms[key])}")

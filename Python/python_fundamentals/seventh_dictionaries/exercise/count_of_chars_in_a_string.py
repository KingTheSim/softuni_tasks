words = input().split()

letters = {}
for word in words:
    for char in word:
        if char not in letters:
            letters[char] = 0
        letters[char] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")

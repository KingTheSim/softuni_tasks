letters = input()

letters = letters.lower()
result = letters.count("sand") + letters.count("water") + letters.count("fish") + letters.count("sun")

print(result)

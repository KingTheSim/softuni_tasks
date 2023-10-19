text = input().split()

final = ""
for word in text:
    final += word * len(word)

print(final)

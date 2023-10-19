target = input()
text = input()

while target in text:
    text = text.replace(target, "")
print(text)

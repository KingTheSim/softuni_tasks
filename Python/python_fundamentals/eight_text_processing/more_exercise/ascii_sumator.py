start = ord(input())
finish = ord(input())
text = input()

result = 0
for ch in text:
    if start < ord(ch) < finish:
        result += ord(ch)

print(result)
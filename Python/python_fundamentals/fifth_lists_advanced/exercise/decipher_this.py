def converter(numbers):
    whole = ""
    for i in numbers:
        whole += i
    whole = int(whole)
    return chr(whole)


words = input().split()

for word in words:
    current_num = []
    current_chars = []
    for ch in word:
        if ch.isdigit():
            current_num.append(ch)
        else:
            current_chars.append(ch)
    new_char = converter(current_num)
    current_chars[0], current_chars[-1] = current_chars[-1], current_chars[0]
    current_chars.insert(0, new_char)
    new_word = "".join(current_chars)
    print(new_word, end=" ")
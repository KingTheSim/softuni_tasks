text = input().split()

start_lower = 97
start_upper = 65
result = 0
for word in text:
    word = word.strip()
    current_num = int(word[1:-1: 1])

    if word[0].islower():
        current_num *= ord(word[0]) - start_lower + 1
    else:
        current_num /= ord(word[0]) - start_upper + 1

    if word[-1].islower():
        current_num += ord(word[-1]) - start_lower + 1
    else:
        current_num -= ord(word[-1]) - start_upper + 1

    result += current_num

print(f"{result:.2f}")

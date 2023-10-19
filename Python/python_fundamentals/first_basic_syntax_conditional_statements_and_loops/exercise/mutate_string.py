import re

first_word = input()
second_word = input()

old_word = ""
new_word = ""

prints = []

for l1 in range(len(first_word)):
    if first_word == second_word:
        print(first_word)
        break

    old_word += first_word[l1]

    for l2 in range(l1 +1):
        if l1 != l2:
            continue

        new_word += second_word[l2]

        if old_word != new_word:
            diff = re.sub(old_word, new_word, first_word, l1 + 1)
            print(diff)
            prints.append(diff)
            if diff == second_word:
                exit()
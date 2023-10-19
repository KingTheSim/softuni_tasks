word_input = input()

word_list = list(word_input)
list_index = list(range(len(word_input)))
counter = 0
for char in word_list:
    if not 65 <= ord(char) <= 90:
        list_index.remove(counter)

    counter += 1
print(list_index)

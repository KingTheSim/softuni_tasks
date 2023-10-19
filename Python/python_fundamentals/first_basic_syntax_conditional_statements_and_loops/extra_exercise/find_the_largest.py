number_input = input()

number_list = list(number_input)
new_number = ""
for i in number_input:
    new_number += max(number_list)
    number_list.remove(max(number_list))

print(new_number)

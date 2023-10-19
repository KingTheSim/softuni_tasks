numbers = input().split()
string = input()

string_list = []
for a in string:
    string_list.append(a)

for number in numbers:
    current = number
    result = 0
    for i in current:
        current_num = int(i)
        result += current_num
    if result > len(string_list) - 1:
        result = result % len(string_list)
    print(string_list[result], end="")
    string_list.pop(result)

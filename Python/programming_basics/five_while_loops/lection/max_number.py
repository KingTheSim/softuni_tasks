import sys
max_num = -sys.maxsize
while True:
    entry = input()
    if entry == "Stop":
        break
    current_num = int(entry)
    if max_num < current_num:
        max_num = current_num
print(max_num)

import sys
min_num = sys.maxsize
while True:
    entry = input()
    if entry == "Stop":
        break
    current_num = int(entry)
    if min_num > current_num:
        min_num = current_num
print(min_num)

number = int(input())
result = 0
while True:
    current_num = int(input())
    result += current_num
    if result >= number:
        print(result)
        break

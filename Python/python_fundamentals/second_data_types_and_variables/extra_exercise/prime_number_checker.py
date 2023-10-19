a = int(input())

flag = True
for i in range(2, a - 1):
    if a % i == 0:
        flag = False
        break

print(flag)

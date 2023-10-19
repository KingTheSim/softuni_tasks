n = int(input())

opened = False
closed = False
for _ in range(n):
    line = input()
    if line == "(" and opened:
        closed = False
        break
    elif line == "(":
        opened = True
        closed = False
    elif line == ")" and opened:
        closed = True
        opened = False
    elif line == ")":
        closed = False
        break

if closed:
    print("BALANCED")
else:
    print("UNBALANCED")

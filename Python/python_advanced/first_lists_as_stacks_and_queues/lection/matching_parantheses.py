starting = input()

parantheses = []
for ind, ch in enumerate(starting):
    if ch == "(":
        parantheses.append(ind)
    elif ch == ")":
        start = parantheses.pop()
        print(starting[start:ind + 1])

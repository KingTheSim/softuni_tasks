from collections import deque

parentheses = deque(input())
opening_parentheses = deque()

while parentheses:
    cur = parentheses.popleft()

    if cur in ["(", "[", "{"]:
        opening_parentheses.append(cur)

    else:
        if not opening_parentheses:
            print("NO")
            break

        else:
            opener = opening_parentheses.pop()
            if f"{opener + cur}" in "(){}[]":
                continue
            else:
                print("NO")
                break

else:
    print("YES")

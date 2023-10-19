n = int(input())

for _ in range(n):
    pure = True
    word = input()
    for ch in word:
        if ch == "," or ch == "." or ch == "_":
            pure = False
            break

    if pure:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")

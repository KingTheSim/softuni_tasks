allowed = ["-", "_"]

possibles = input().split(", ")

for word in possibles:
    if 3 <= len(word) <= 16:
        broken = False
        for ch in word:
            if not ch.isalnum() and ch not in allowed:
                broken = True
                break
        if not broken:
            print(word)

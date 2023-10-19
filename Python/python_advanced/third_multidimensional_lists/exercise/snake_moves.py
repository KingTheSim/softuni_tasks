from collections import deque
rows, cols = [int(x) for x in input().split()]

word_original = deque(input())
word_current = word_original.copy()

for r in range(rows):
    while len(word_current) < cols:
        word_current += deque(word_original)

    if r % 2 == 0:
        print(*[word_current.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word_current.popleft() for _ in range(cols)][::-1], sep="")

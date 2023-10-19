all_nums = [int(x) for x in input().split(", ")]

positives = [str(a) for a in all_nums if a >= 0]
negatives = [str(b) for b in all_nums if b < 0]
evens = [str(c) for c in all_nums if c % 2 == 0]
odds = [str(d) for d in all_nums if d % 2 != 0]

print("Positive: ", end="")
print(", ".join(positives))
print("Negative: ", end="")
print(", ".join(negatives))
print("Even: ", end="")
print(", ".join(evens))
print("Odd: ", end="")
print(", ".join(odds))

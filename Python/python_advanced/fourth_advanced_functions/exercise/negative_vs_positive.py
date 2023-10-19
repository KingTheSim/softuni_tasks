def seperator(*args):
    pos = [a for a in args if a > 0]
    neg = [b for b in args if b < 0]
    return sum(pos), sum(neg)


nums = [int(x) for x in input().split()]
positives, negatives = seperator(*nums)

print(negatives)
print(positives)

if positives > abs(negatives):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")

def miner(numbers):
    smallest = float("inf")
    for a in numbers:
        if a < smallest:
            smallest = a
    return smallest


def maxer(numbers):
    biggest = float("-inf")
    for b in numbers:
        if b > biggest:
            biggest = b
    return biggest


def summer(numbers):
    total = 0
    for c in numbers:
        total += c
    return total


nums = [int(x) for x in input().split()]

print(f"The minimum number is {miner(nums)}")
print(f"The maximum number is {maxer(nums)}")
print(f"The sum number is: {summer(nums)}")

def smallest(nums):
    min_num = float("inf")
    for n in nums:
        if n < min_num:
            min_num = n
    return min_num


first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
print(smallest(numbers))

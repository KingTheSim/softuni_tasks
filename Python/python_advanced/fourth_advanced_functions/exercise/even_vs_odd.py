def even_odd(*args):
    nums, kind = args[:-1], args[-1]
    if kind == "even":
        return [x for x in nums if x % 2 == 0]
    else:
        return [x for x in nums if x % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

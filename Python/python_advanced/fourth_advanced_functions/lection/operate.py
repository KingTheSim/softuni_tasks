def operate(op, *args):
    if op == "+":
        return sum(args)
    elif op == "-":
        res = args[0]
        if len(args) != 1:
            for i in range(1, len(args)):
                res -= args[i]
        return res
    elif op == "*":
        res = 1
        for i in args:
            res *= i
        return res
    else:
        res = args[0]
        if len(args) != 1:
            for i in range(1, len(args)):
                res /= args[i]
        return res


print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))
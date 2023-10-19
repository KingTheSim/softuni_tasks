cash = float(input())
start_cur = input()
finish_cur = input()

bgn = 0
if start_cur == "BGN":
    bgn = cash
elif start_cur == "USD":
    bgn = cash * 1.79549
elif start_cur == "EUR":
    bgn = cash * 1.95583
else:
    bgn = cash * 2.53405

result = 0
if finish_cur == "BGN":
    result = bgn
elif finish_cur == "USD":
    result = bgn / 1.79549
elif finish_cur == "EUR":
    result = bgn / 1.95583
else:
    result = bgn / 2.53405

print(f"{result:.2f} {finish_cur}")

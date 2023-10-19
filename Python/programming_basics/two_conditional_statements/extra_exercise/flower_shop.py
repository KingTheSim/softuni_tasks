from math import floor, ceil

# known
fp1 = 3.25  # price for the magnolis
fp2 = 4  # price for the zyumbyuls
fp3 = 3.50  # price for the roses
fp4 = 8  # price for the cactuses
# the government tax is 5%

# user input
number_f1 = int(input())
number_f2 = int(input())
number_f3 = int(input())
number_f4 = int(input())
present_price = float(input())

# logic
pf1_final = fp1 * number_f1
pf2_final = fp2 * number_f2
pf3_final = fp3 * number_f3
pf4_final = fp4 * number_f4
pf_total = (pf1_final + pf2_final + pf3_final + pf4_final) * 0.95

# code output
if pf_total >= present_price:
    print(f"She is left with {floor(pf_total - present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - pf_total)} leva.")

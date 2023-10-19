# user input
months = int(input())

# logic
el = 0
water = 0
internet = 0
others = 0
for i in range(months):
    current_el = float(input())
    el += current_el
    water += 20
    internet += 15
    others += (current_el + 20 + 15) * 1.2

av_paid = (el + water + internet + others) / months

# code output
print(f"Electricity: {el:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {av_paid:.2f} lv")

# known
n = 24 * 60
# logic and output
hours = 0
minutes = 0
for i in range(n):
    if minutes == 60:
        minutes = 0
        hours += 1
    print(f"{hours} : {minutes}")
    minutes += 1

# known
n = 24 * 60 * 60

# logic and output
hours = 0
minutes = 0
seconds = 0
for i in range(n):
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    print(f"{hours} : {minutes} : {seconds}")
    seconds += 1

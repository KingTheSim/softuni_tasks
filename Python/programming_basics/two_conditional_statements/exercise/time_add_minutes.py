# user input
input_hours = int(input())
input_minutes = int(input())

# logic
total_minutes = (input_hours * 60) + input_minutes + 15
hours = total_minutes // 60
minutes = total_minutes % 60

# code output
if hours >= 24:
    print(f"{0}:{minutes:02d}")
else:
    print(f"{hours}:{minutes:02d}")

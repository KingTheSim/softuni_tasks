# known
target = 10000

# user input
input_line = input()

# logic
steps = 0
goal = False

while input_line != "Going home":
    current_steps = int(input_line)
    steps += current_steps
    if steps >= target:
        goal = True
        break
    input_line = input()

if input_line == "Going home":
    current_steps = int(input())
    steps += current_steps
    if steps >= target:
        goal = True
diff = abs(target - steps)

# code output
if goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

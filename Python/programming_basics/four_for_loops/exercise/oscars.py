# user input
actor = input()
init_points = float(input())
n = int(input())

# logic
refer = ""
points = 0
current_points = init_points
nominee = False

for i in range(n):
    refer = input()
    points = float(input())
    length = len(refer)
    current_points += (length * points) / 2

    if current_points >= 1250.5:
        nominee = True
        break

diff = abs(current_points - 1250.5)

# code output
if nominee:
    print(f"Congratulations, {actor} got a nominee for leading role with {current_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {diff:.1f} more!")

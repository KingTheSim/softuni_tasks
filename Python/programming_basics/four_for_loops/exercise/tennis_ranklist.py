from math import floor

# user input
n = int(input())
initial_points = int(input())

# logic
points = initial_points
wins = 0
for i in range(n):
    result = input()
    if result == "W":
        points += 2000
        wins += 1
    elif result == "F":
        points += 1200
    else:
        points += 720

aver_points = (points - initial_points) / n
wins_perc = wins / n * 100

# code output
print(f"Final points: {points}")
print(f"Average points: {floor(aver_points)}")
print(f"{wins_perc:.2f}%")

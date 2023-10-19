line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

first_won = False
second_won = False
if line_1[0] == line_1[1] == line_1[2] == "1":
    first_won = True
elif line_1[0] == line_1[1] == line_1[2] == "2":
    second_won = True
elif line_2[0] == line_2[1] == line_2[2] == "1":
    first_won = True
elif line_2[0] == line_2[1] == line_2[2] == "2":
    second_won = True
elif line_3[0] == line_3[1] == line_3[2] == "1":
    first_won = True
elif line_3[0] == line_3[1] == line_3[2] == "2":
    second_won = True
elif line_1[0] == line_2[1] == line_3[2] == "1":
    first_won = True
elif line_1[0] == line_2[1] == line_3[2] == "2":
    second_won = True
elif line_3[0] == line_2[1] == line_1[2] == "1":
    first_won = True
elif line_3[0] == line_2[1] == line_1[2] == "2":
    second_won = True
elif line_1[0] == line_2[0] == line_3[0] == "1":
    first_won = True
elif line_1[0] == line_2[0] == line_3[0] == "2":
    second_won = True
elif line_1[1] == line_2[1] == line_3[1] == "1":
    first_won = True
elif line_1[1] == line_2[1] == line_3[1] == "2":
    second_won = True
elif line_1[2] == line_2[2] == line_3[2] == "1":
    first_won = True
elif line_1[2] == line_2[2] == line_3[2] == "2":
    second_won = True

if first_won:
    print("First player won")
elif second_won:
    print("Second player won")
else:
    print("Draw!")

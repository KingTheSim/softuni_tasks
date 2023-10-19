target = float(input())

reached_flag = False
cash = 0
while True:
    service = input()
    if service == "closed":
        break
    type_service = input()
    if service == "haircut":
        if type_service == "mens":
            cash += 15
        elif type_service == "ladies":
            cash += 20
        else:
            cash += 10
    else:
        if type_service == "touch up":
            cash += 20
        else:
            cash += 30
    if cash >= target:
        reached_flag = True
        break

if reached_flag:
    print("You have reached your target for the day!")
else:
    diff = abs(cash - target)
    print(f"Target not reached! You need {round(diff)}lv. more.")
print(f"Earned money: {round(cash)}lv.")

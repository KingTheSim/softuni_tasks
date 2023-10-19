num = int(input())

parking = {}
for _ in range(num):
    info = input().split()

    if info[0] == "register":
        if info[1] in parking:
            print(f"ERROR: already registered with plate number {parking[info[1]]}")
        else:
            parking[info[1]] = info[2]
            print(f"{info[1]} registered {info[2]} successfully")

    else:
        if info[1] in parking:
            del parking[info[1]]
            print(f"{info[1]} unregistered successfully")
        else:
            print(f"ERROR: user {info[1]} not found")

for key, value in parking.items():
    print(f"{key} => {value}")

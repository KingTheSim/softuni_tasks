floors = int(input())
rooms = int(input())
floor_nm = ""
room_type = ""
for floor_nm in range(floors, 0, -1):
    for rooms_nm in range(0, rooms):
        if floor_nm == floors:
            room_type = "L"
        elif floor_nm % 2 != 0:
            room_type = "A"
        else:
            room_type = "O"
        print(f"{room_type}{floor_nm}{rooms_nm}", end=" ")
    print()

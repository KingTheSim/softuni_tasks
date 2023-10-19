# user input
width = int(input())
length = int(input())
height = int(input())

# logic
volume = width * length * height
comm = input()
filled = 0
finish = False
while comm != "Done":
    boxes = int(comm)
    filled += boxes
    if filled >= volume:
        finish = True
        break
    comm = input()
diff = abs(volume - filled)

# code output
if finish:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")

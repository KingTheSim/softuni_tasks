# user input
width = int(input())
length = int(input())

# logic
pieces = width * length
comm = input()
taken = 0
finish = False

while comm != "STOP":
    taken += int(comm)
    if taken >= pieces:
        finish = True
        break
    comm = input()

diff = abs(pieces - taken)

# code output
if finish:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")

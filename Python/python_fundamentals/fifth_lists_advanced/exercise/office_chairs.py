rooms = int(input())

failed = False
total_left = 0
for i in range(1, rooms + 1):
    current = input().split()
    people = int(current[1])
    compared = len(current[0]) - people
    if compared < 0:
        print(f"{abs(compared)} more chairs needed in room {i}")
        failed = True
    else:
        total_left += compared

if not failed:
    print(f"Game On, {total_left} free chairs left")

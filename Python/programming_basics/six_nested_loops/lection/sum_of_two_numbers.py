starting = int(input())
finishing = int(input())
magic_num = int(input())

counter = 0
found = False
for a in range(starting, finishing + 1):
    for b in range(starting, finishing + 1):
        counter += 1
        if a + b == magic_num:
            print(f"Combination N:{counter} ({a} + {b} = {magic_num})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{counter} combinations - neither equals {magic_num}")

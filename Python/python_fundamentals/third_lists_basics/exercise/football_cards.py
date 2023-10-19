cards = input().split()

A_counter = 0
B_counter = 0
encountered = []
ended = False
for card in cards:
    if card in encountered:
        continue
    encountered.append(card)

    if card[0] == "A":
        A_counter += 1
    else:
        B_counter += 1

    if A_counter > 4 or B_counter > 4:
        ended = True
        break

print(f"Team A - {11 - A_counter}; Team B - {11 - B_counter}")
if ended:
    print("Game was terminated")

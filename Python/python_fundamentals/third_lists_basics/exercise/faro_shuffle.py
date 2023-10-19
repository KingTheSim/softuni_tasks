cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    first_half = []
    second_half = []
    suffled = []
    for i in range(1, len(cards) - 1):
        card = cards[i]

        if i < len(cards) / 2:
            first_half.append(card)
        else:
            second_half.append(card)

    first_ind = 0
    second_ind = 0
    for ind in range(len(first_half) * 2):
        if ind % 2 != 0:
            suffled.append(first_half[first_ind])
            first_ind += 1
        else:
            suffled.append(second_half[second_ind])
            second_ind += 1

    cards = [cards[0]] + suffled + [cards[-1]]

print(cards)

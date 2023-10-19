def validator(index, cards):
    return 0 <= index < len(cards)


start_cards = input().split(", ")
n = int(input())

new_deck = start_cards
for _ in range(n):
    command = input().split(", ")
    if command[0] == "Add":
        if command[1] in new_deck:
            print("Card is already in the deck")
            continue
        new_deck.append(command[1])
        print("Card successfully added")

    elif command[0] == "Remove":
        if command[1] not in new_deck:
            print("Card not found")
            continue
        new_deck.remove(command[1])
        print("Card successfully removed")

    elif command[0] == "Remove At":
        ind = int(command[1])
        if not validator(ind, new_deck):
            print("Index out of range")
            continue
        new_deck.pop(ind)
        print("Card successfully removed")

    else:
        ind = int(command[1])
        if validator(ind, new_deck):
            if command[2] in new_deck:
                print("Card is already added")
                continue
            new_deck.insert(ind, command[2])
            print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(new_deck))

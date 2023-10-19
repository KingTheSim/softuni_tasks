class Party:
    def __init__(self):
        self.people = []


total = 0
party = Party()
while True:
    text = input()
    if text == "End":
        break
    party.people.append(text)
    total += 1

people = ", ".join(party.people)
print(f"Going: {people}")
print(f"Total: {total}")

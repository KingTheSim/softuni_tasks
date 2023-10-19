contacts = {}
while True:
    current = input()
    if current.isdigit():
        break
    name, numbers = current.split("-")
    contacts[name] = numbers

number = int(current)
for _ in range(number):
    needed = input()
    if needed in contacts:
        print(f"{needed} -> {contacts[needed]}")
    else:
        print(f"Contact {needed} does not exist.")

# user input
name = input()
orig = input()

# logic
while True:
    pw = input()
    if pw != orig:
        continue
    else:
        print(f"Welcome {name}!")
        break

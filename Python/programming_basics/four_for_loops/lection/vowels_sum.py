# user input
text = input()

# logic
num = 0
for char in text:
    if char == "a":
        num = num + 1
    elif char == "e":
        num = num + 2
    elif char == "i":
        num = num + 3
    elif char == "o":
        num = num + 4
    elif char == "u":
        num = num + 5
    else:
        continue
print(num)

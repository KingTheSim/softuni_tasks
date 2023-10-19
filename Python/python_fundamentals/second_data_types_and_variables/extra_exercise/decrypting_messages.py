n = int(input())
lines = int(input())

for i in range(lines):
    letter = ord(input())
    letter += n
    print(chr(letter), end="")

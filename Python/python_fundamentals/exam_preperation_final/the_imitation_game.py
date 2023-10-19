original = input()

result = original
while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    if command[0] == "Move":
        result = result[int(command[1]):] + result[:int(command[1])]
    elif command[0] == "Insert":
        result = result[:int(command[1])] + command[2] + result[int(command[1]):]
    elif command[0] == "ChangeAll":
        result = result.replace(command[1], command[2])

print(f"The decrypted message is: {result}")

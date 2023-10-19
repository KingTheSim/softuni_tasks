# user input
n = int(input())

# logic
detergent = n * 750
dishes = 0
pots = 0
command = input()
count = 0
while True:
    if command == "End":
        break
    number = int(command)
    count += 1
    if count % 3 == 0:
        detergent -= number * 15
        pots += number
    else:
        detergent -= number * 5
        dishes += number
    if detergent < 0:
        break
    command = input()
diff = abs(detergent)

# output
if detergent < 0:
    print(f"Not enough detergent, {diff} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")

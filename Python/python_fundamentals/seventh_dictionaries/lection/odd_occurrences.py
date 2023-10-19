words = input().lower().split(" ")

ocur = {}
for word in words:
    if word not in ocur:
        ocur[word] = 0
    ocur[word] += 1

for key, value in ocur.items():
    if value % 2 != 0:
        print(key, end=" ")

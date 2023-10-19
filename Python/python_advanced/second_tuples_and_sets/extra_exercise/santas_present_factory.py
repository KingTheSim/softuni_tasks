from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

finished = []
fin_set = set()

recipie = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic:
    cur_mat = materials.pop()
    cur_magic = magic.popleft()

    if cur_mat == 0 and cur_magic == 0:
        continue
    elif cur_mat == 0:
        magic.appendleft(cur_magic)
        continue
    elif cur_magic == 0:
        materials.append(cur_mat)
        continue

    result = cur_mat * cur_magic

    if result in recipie:
        finished.append(recipie[result])
        fin_set.add(recipie[result])
    elif result < 0:
        materials.append(cur_mat + cur_magic)
    else:
        materials.append(cur_mat + 15)

targets_1 = {"Doll", "Wooden train"}
target_2 = {"Teddy bear", "Bicycle"}

if targets_1.issubset(finished) or target_2.issubset(finished):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for toy in sorted(fin_set):
    print(f"{toy}: {finished.count(toy)}")

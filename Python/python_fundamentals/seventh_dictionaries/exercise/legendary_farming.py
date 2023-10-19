farmed = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
reached = False
while not reached:
    info = input().split()
    for i in range(0, len(info), 2):
        quan = int(info[i])
        mat = info[i + 1].lower()

        if mat in farmed:
            farmed[mat] += quan
            if farmed[mat] >= 250:
                if mat == "shards":
                    print("Shadowmourne obtained!")
                elif mat == "fragments":
                    print("Valanyr obtained!")
                else:
                    print("Dragonwrath obtained!")
                farmed[mat] -= 250
                reached = True
                break

        else:
            if mat not in junk:
                junk[mat] = 0
            junk[mat] += quan

for key, value in farmed.items():
    print(f"{key}: {value}")

for j, v in junk.items():
    print(f"{j}: {v}")

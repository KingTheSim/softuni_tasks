import re

pattern = r"^>>(?P<furniture>[A-Za-z]+)<<(?P<price>[0-9]+([\.][0-9]+)?)!(?P<quantity>\d+)$"
found = ""
while True:
    command = input()
    if command == "Purchase":
        break
    if re.search(pattern, command):
        if found == "":
            found += command
        else:
            found += ", " + command

final_pattern = r"^>>(?P<furniture>[A-Za-z]+)<<(?P<price>[0-9]+([\.][0-9]+)?)!(?P<quantity>\d+)$"
resulting = re.finditer(final_pattern, found)
total = 0
furniture = []
for match in resulting:
    cur_dict = match.groupdict()
    furniture.append(cur_dict["furniture"])
    total += float(cur_dict["price"]) * int(cur_dict["quantity"])

print("Bought furniture:")
if furniture:
    for furn in furniture:
        print(furn)
print(f"Total money spend: {total:.2f}")

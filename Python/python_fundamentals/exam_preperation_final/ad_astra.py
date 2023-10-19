import re

items = input()

pattern = r"#(?P<product1>[A-Za-z\s]+)#(?P<date1>\d{2}\/\d{2}\/\d{2})#(?P<calories1>\d+)#|" \
          r"\|(?P<product2>[A-Za-z\s]+)\|(?P<date2>\d{2}\/\d{2}\/\d{2})\|(?P<calories2>\d+)\|"
matches = re.finditer(pattern, items)
total_cals = 0
info = []

for match in matches:
    current = match.groupdict()
    if current["product1"] is not None:
        total_cals += int(current["calories1"])
        info.append(f"Item: {current['product1']}, Best before: {current['date1']}, Nutrition: {current['calories1']}")
    else:
        total_cals += int(current["calories2"])
        info.append(f"Item: {current['product2']}, Best before: {current['date2']}, Nutrition: {current['calories2']}")

print(f"You have food to last you for: {int(total_cals / 2000)} days!")
for i in info:
    print(i)

import re

number = int(input())

pattern = r"@\#+(?P<product>[A-Z][A-Za-z0-9]{4,}[A-Z])@\#+"
for _ in range(number):
    current = input()

    if re.match(pattern, current):
        result = ""
        for ch in current:
            if ch.isdigit():
                result += ch

        if result:
            print(f"Product group: {result}")
        else:
            print(f"Product group: 00")

    else:
        print("Invalid barcode")

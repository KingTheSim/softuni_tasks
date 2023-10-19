import re

number = int(input())

pattern = r"(.+)>(?P<num>\d{3})\|(?P<lower>[a-z]{3})\|(?P<upper>[A-Z]{3})\|(?P<chars>[^<>]{3})<\1"
for _ in range(number):
    current = re.finditer(pattern, input())
    password = ""
    continued = False
    for match in current:
        current_dict = match.groupdict()
        password += current_dict["num"] + current_dict["lower"] + current_dict["upper"] + current_dict["chars"]
        print(f"Password: {password}")
        continued = True
        continue
    if continued:
        continue
    else:
        print("Try another password!")

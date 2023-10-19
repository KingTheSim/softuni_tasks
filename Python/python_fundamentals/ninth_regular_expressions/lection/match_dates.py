import re

text = input()

pattern = r"\b(?P<Day>\d{2})([\.\/-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
dates = re.finditer(pattern, text)

for date in dates:
    data_date = date.groupdict()
    print(f"Day: {data_date['Day']}, Month: {data_date['Month']}, Year: {data_date['Year']}")

text = input()

letters = set()
for el in text:
    letters.add(el)

for lt in sorted(letters):
    print(f"{lt}: {text.count(lt)} time/s")

text = input()

banned = ['a', 'o', 'u', 'e', 'i']
result = [x for x in text if x.lower() not in banned]

print("".join(result))

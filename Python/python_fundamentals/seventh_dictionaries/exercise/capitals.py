countries = tuple(input().split(", "))
capitals = tuple(input().split(", "))

paired = dict(zip(countries, capitals))

for count, cap in paired.items():
    print(f"{count} -> {cap}")

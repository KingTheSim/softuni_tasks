first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

funcs = {
    "Add First": lambda x: [first.add(int(el)) for el in x],
    "Add Second": lambda x: [second.add(int(el)) for el in x],
    "Remove First": lambda x: [first.discard(int(el)) for el in x],
    "Remove Second": lambda x: [second.discard(int(el)) for el in x],
    "Check Subset": lambda x: print(first.issubset(second) or second.issubset(first))
}

for _ in range(int(input())):
    first_com, second_com, *data = input().split()
    whole_com = first_com + " " + second_com

    if data:
        data = [int(x) for x in data]

    funcs[whole_com](data)

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")

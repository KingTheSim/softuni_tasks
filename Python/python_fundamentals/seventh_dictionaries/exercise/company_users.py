companies = {}
while True:
    command = input()
    if command == "End":
        break

    comp, identity = command.split(" -> ")
    if comp not in companies:
        companies[comp] = []
    if identity not in companies[comp]:
        companies[comp].append(identity)

for name, idents in companies.items():
    print(name)
    for ident in idents:
        print(f"-- {ident}")

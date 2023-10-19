def dfs(node, struct, been, path):
    if node in path:
        raise Exception
    if node in been:
        return
    visited.add(node)
    path.add(node)

    for child in struct[node]:
        dfs(child, struct, been, path)

    path.remove(node)


graph = {}
while True:
    command = input().split("-")
    if command[0] == "End":
        break
    else:
        if command[0] not in graph:
            graph[command[0]] = []
        graph[command[0]].append(command[1])
        if command[1] not in graph:
            graph[command[1]] = []

visited = set()
cycle = False

try:
    for source in graph:
        dfs(source, graph, visited, set())
except Exception:
    cycle = True

if cycle:
    print(f"Acyclic: No")
else:
    print(f"Acyclic: Yes")

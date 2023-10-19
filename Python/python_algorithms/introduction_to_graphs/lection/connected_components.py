def dfs(node, struct, been, component):
    if been[node]:
        return
    else:
        been[node] = True

    for child in struct[node]:
        dfs(child, struct, been, component)

    component.append(node)


node_numbers = int(input())
graph = {}

for i in range(node_numbers):
    line = input()
    current = [] if line == "" else [int(x) for x in line.split()]
    graph[i] = current

visited = [False] * len(graph)
for cur in graph:
    if visited[cur]:
        continue
    now = []
    dfs(cur, graph, visited, now)
    print("Connected component:", end=" ")
    print(*now, sep=" ")
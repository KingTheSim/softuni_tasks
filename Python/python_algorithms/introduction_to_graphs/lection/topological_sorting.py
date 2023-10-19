def predecessor_counter(struct):
    result = {}
    for predecessor, heirs in struct.items():
        if predecessor not in result:
            result[predecessor] = 0
        for heir in heirs:
            if heir not in result:
                result[heir] = 1
            else:
                result[heir] += 1
    return result


def independent_finder(current):
    for node, value in current.items():
        if value == 0:
            return node
    return None


nodes_number = int(input())

graph = {}
for _ in range(nodes_number):
    line = input().split("->")
    parent = line[0].strip()
    children = line[1].strip().split(", ") if line[1] else []
    graph[parent] = children

sorted_nodes = []
dependent = predecessor_counter(graph)
while dependent:
    remove_target = independent_finder(dependent)
    if remove_target is None:
        print("Invalid topological sorting")
        break
    sorted_nodes.append(remove_target)
    dependent.pop(remove_target)
    for child in graph[remove_target]:
        dependent[child] -= 1
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")

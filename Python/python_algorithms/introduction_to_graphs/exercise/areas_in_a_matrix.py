def dfs(row, col, graph, been, last):
    if row < 0 or row >= len(graph):
        return
    elif col < 0 or col >= len(graph[row]):
        return
    elif been[row][col]:
        return
    elif last != graph[row][col]:
        return

    been[row][col] = True
    dfs(row + 1, col, graph, been, graph[row][col])
    dfs(row - 1, col, graph, been, graph[row][col])
    dfs(row, col + 1, graph, been, graph[row][col])
    dfs(row, col - 1, graph, been, graph[row][col])


n = int(input())
m = int(input())

visited = []
matrix = []
for _ in range(n):
    matrix.append(list(input()))
    visited.append([False] * m)

total_areas = 0
areas = {}
for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            total_areas += 1
            if matrix[r][c] not in areas:
                areas[matrix[r][c]] = 1
            else:
                areas[matrix[r][c]] += 1
            cur = matrix[r][c]
            dfs(r, c, matrix, visited, cur)

print(f"Areas: {total_areas}")
sorted_areas = dict(sorted(areas.items()))
for area, number in sorted_areas.items():
    print(f"Letter '{area}' -> {number}")

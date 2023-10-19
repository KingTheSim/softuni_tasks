def solutions_finder(inx, goal, all_indexes, all_counts, used_parts):
    if inx >= len(goal):
        print(" ".join(used_parts))
        return
    if inx not in all_indexes:
        return
    for word in all_indexes[inx]:
        if all_counts[word] == 0:
            continue
        used_parts.append(word)
        all_counts[word] -= 1
        solutions_finder(inx + len(word), goal, all_indexes, all_counts, used_parts)
        all_counts[word] += 1
        used_parts.pop()


parts = input().split(", ")
target = input()

indexes = {}
counts = {}
for part in parts:
    if part in counts:
        counts[part] += 1
        continue

    counts[part] = 1

    try:
        index = 0
        while True:
            index = target.index(part, index)
            if index not in indexes:
                indexes[index] = []
            indexes[index].append(part)
            index += len(part)
    except ValueError:
        pass

solutions_finder(0, target, indexes, counts, [])
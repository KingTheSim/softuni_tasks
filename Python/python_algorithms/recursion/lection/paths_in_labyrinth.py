def pathfinder(lab, row, col, direction, actions):
    if row > len(lab) - 1 or row < 0:
        return
    elif col > len(lab[row]) - 1 or col < 0:
        return
    elif lab[row][col] == "*" or lab[row][col] == "v":
        return
    elif lab[row][col] == "e":
        actions.append(direction)
        print("".join(actions))
    else:
        lab[row][col] = "v"
        actions.append(direction)
        pathfinder(lab, row, col + 1, "R", actions)
        pathfinder(lab, row, col - 1, "L", actions)
        pathfinder(lab, row - 1, col, "U", actions)
        pathfinder(lab, row + 1, col, "D", actions)
        lab[row][col] = "-"
    actions.pop()


x = int(input())
y = int(input())

labyrinth = []
for _ in range(x):
    labyrinth.append([a for a in input()])
pathfinder(labyrinth, 0, 0, "", [])

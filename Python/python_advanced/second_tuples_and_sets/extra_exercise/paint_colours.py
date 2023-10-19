the_line = input().split()

main = {"red","yellow", "blue"}
secondary = {"orange", "purple", "green"}
found = set()

while the_line:
    if len(the_line) != 1:
        cur_left = the_line.pop(0)
        cur_right = the_line.pop()

        if cur_left + cur_right in main or cur_left + cur_right in secondary:
            found.add(cur_left + cur_right)
        elif cur_right + cur_left in main or cur_right + cur_left in secondary:
            found.add(cur_right + cur_left)
        else:
            middle = len(the_line) // 2 + 1
            the_line.insert(middle, cur_right[:-1])
            the_line.insert(middle, cur_left[:-1])
    else:
        if the_line[0] in main or the_line[0] in secondary:
            found.add(the_line.pop())


def lists_merger(current_left, current_right):
    result = []
    while current_left and current_right:
        if current_left[0] > current_right[0]:
            result.append(current_right[0])
            current_right.remove(current_right[0])
        else:
            result.append(current_left[0])
            current_left.remove(current_left[0])
    else:
        if current_right:
            for el_right in current_right:
                result.append(el_right)
        else:
            for el_left in current_left:
                result.append(el_left)
    return result


def merge_sorter(nums_list):
    if len(nums_list) == 1:
        return nums_list

    mid_inx = len(nums_list) // 2
    left_part = nums_list[:mid_inx]
    right_part = nums_list[mid_inx:]

    return lists_merger(merge_sorter(left_part), merge_sorter(right_part))


nums = [int(x) for x in input().split()]

print(*merge_sorter(nums), sep=" ")

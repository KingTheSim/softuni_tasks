def lists_merger(current_left, current_right):
    result = [None] * (len(current_left) + len(current_right))
    left_inx = 0
    right_inx = 0
    result_inx = 0

    while left_inx < len(current_left) and right_inx < len(current_right):
        if current_left[left_inx] < current_right[right_inx]:
            result[result_inx] = current_left[left_inx]
            left_inx += 1
        else:
            result[result_inx] = current_right[right_inx]
            right_inx += 1
        result_inx += 1

    while left_inx < len(current_left):
        result[result_inx] = current_left[left_inx]
        left_inx += 1
        result_inx += 1

    while right_inx < len(current_right):
        result[result_inx] = current_right[right_inx]
        right_inx += 1
        result_inx += 1


def merge_sorter(nums_list):
    if len(nums_list) == 1:
        return nums_list

    mid_inx = len(nums_list) // 2
    left_part = nums_list[:mid_inx]
    right_part = nums_list[mid_inx:]

    return lists_merger(merge_sorter(left_part), merge_sorter(right_part))


nums = [int(x) for x in input().split()]

print(*merge_sorter(nums), sep=" ")

def binary_searcher(number_list, goal):
    left = 0
    right = len(number_list) - 1
    while left <= right:
        mid_inx = (right + left) // 2
        mid_el = number_list[mid_inx]
        if mid_el == goal:
            return mid_inx
        elif mid_el > goal:
            right = mid_inx - 1
        else:
            left = mid_inx + 1
    else:
        return -1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_searcher(nums, target))

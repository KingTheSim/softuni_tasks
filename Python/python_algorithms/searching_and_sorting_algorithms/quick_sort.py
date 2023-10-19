def quicksorter(start, end, nums_list):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if nums_list[left] > nums_list[pivot] > nums_list[right]:
            nums_list[left], nums_list[right] = nums_list[right], nums_list[left]
        if nums_list[left] <= nums_list[pivot]:
            left += 1
        if nums_list[right] >= nums_list[pivot]:
            right -= 1

    nums_list[pivot], nums_list[right] = nums_list[right], nums_list[pivot]
    quicksorter(pivot, right - 1, nums_list)
    quicksorter(left, end, nums_list)


nums = [int(x) for x in input().split()]

quicksorter(0, len(nums) - 1, nums)
print(*nums, sep=" ")

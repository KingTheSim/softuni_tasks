nums = [int(x) for x in input().split()]

is_sorted = False
counter = 0
while not is_sorted:
    is_sorted = True
    for inx in range(1, len(nums) - counter):
        if nums[inx - 1] > nums[inx]:
            is_sorted = False
            nums[inx - 1], nums[inx] = nums[inx], nums[inx - 1]
    counter += 1

print(*nums, sep=" ")

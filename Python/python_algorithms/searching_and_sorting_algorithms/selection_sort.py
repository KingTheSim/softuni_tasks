nums = [int(x) for x in input().split()]

for inx in range(len(nums)):
    min_number = nums[inx]
    min_inx = inx
    for next_inx in range(inx + 1, len(nums)):
        next_num = nums[next_inx]
        if next_num < min_number:
            min_number = next_num
            min_inx = next_inx
    nums[inx], nums[min_inx] = nums[min_inx], nums[inx]

print(*nums, sep=" ")
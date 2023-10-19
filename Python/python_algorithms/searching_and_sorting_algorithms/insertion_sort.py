nums = [int(x) for x in input().split()]

for j in range(len(nums)):
    for i in range(j, 0, -1):
        if nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]

print(*nums, sep=" ")

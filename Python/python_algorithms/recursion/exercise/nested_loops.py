def looper(nums, inx):
    if inx == len(nums):
        print(*nums, sep=" ")
        return
    else:
        for i in range(1, len(nums) + 1):
            nums[inx] = i
            looper(nums, inx + 1)


n = int(input())

starter = [1] * n
looper(starter, 0)

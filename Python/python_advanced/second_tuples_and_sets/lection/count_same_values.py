nums = (input().split())

counted = {}

for n in nums:
    if n not in counted:
        counted[n] = nums.count(n)

for key, value in counted.items():
    key = float(key)
    print(f"{key:.1f} - {value} times")

import os.path

nums = []

with open(os.path.join("Day 9", "input.txt")) as f:
    for line in f:
        nums.append(int(line))

for n in range(25, len(nums)):
    previous = nums[n-25:n]
    passed = False
    for p in previous:
        if nums[n] - p in previous and nums[n] - p != p:
            passed = True
    if not passed:
        print(nums[n])
        break
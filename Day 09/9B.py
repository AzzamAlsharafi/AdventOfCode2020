import os.path

nums = []

with open(os.path.join("Day 09", "input.txt")) as f:
    for line in f:
        nums.append(int(line))

invalidNum = 0

for n in range(25, len(nums)):
    previous = nums[n-25:n]
    passed = False
    for p in previous:
        if nums[n] - p in previous and nums[n] - p != p:
            passed = True
    if not passed:
        invalidNum = nums[n]
        break

print(invalidNum)

setSize = 2
while True:
    for i in range(len(nums)):
        contiguousNums = nums[i:i+setSize]
        if sum(contiguousNums) == invalidNum:
            print(min(contiguousNums) + max(contiguousNums))
            exit(0)
    setSize += 1
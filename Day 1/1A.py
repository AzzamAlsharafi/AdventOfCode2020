import os.path

nums = []

with open(os.path.join("Day 1", "input.txt")) as f:
    for line in f:
        nums.append(int(line))

for n in nums:
    if 2020-n in nums:
        print(n)
        print(2020-n)
        print(n*(2020-n))
        break
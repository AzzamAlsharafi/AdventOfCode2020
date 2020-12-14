import os.path

nums = []

with open(os.path.join("Day 01", "input.txt")) as f:
    for line in f:
        nums.append(int(line))

newNums = [2020-n for n in nums]

for nn in newNums:
    for n in nums:
        if nn-n in nums:
            print(2020-nn)
            print(n)
            print(nn-n)
            print((2020-nn)*n*(nn-n))
            exit(0)
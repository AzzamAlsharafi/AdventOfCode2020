import os.path

validCounter = 0

def isValid(string):
    policy, password = string.split(": ")
    limits, letter = policy.split()
    lowest, highest = map(int, limits.split("-"))

    if lowest <= password.count(letter) <= highest:
        return True

with open(os.path.join("Day 02", "input.txt")) as f:
    for line in f:
        if isValid(line):
            validCounter += 1

print(validCounter)

import os.path

validCounter = 0

def isValid(string):
    policy, password = string.split(": ")
    limits, letter = policy.split()
    positionA, positionB = map(int, limits.split("-"))

    if (password[positionA - 1] is letter) ^ (password[positionB - 1] is letter):
        return True

with open(os.path.join("Day 02", "input.txt")) as f:
    for line in f:
        if isValid(line):
            validCounter += 1

print(validCounter)

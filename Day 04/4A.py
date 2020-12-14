import os.path

passports = []

with open(os.path.join("Day 04", "input.txt")) as f:
    passports = f.read().split("\n\n")

validCount = 0

for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        validCount += 1

print(validCount)
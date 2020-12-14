import os.path
import re

passports = []

with open(os.path.join("Day 04", "input.txt")) as f:
    passports = f.read().split("\n\n")

validCount = 0

for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        fields = dict([i.split(":") for i in passport.split()])

        if not ((len(fields["byr"]) == 4) and (1920 <= int(fields["byr"]) <= 2002)):
            continue
        if not ((len(fields["iyr"]) == 4) and (2010 <= int(fields["iyr"]) <= 2020)):
            continue
        if not ((len(fields["eyr"]) == 4) and (2020 <= int(fields["eyr"]) <= 2030)):
            continue
        if "cm" in fields["hgt"]:
            if not (150 <= int(fields["hgt"].replace("cm", "")) <= 193):
                continue
        else:
            if not (59 <= int(fields["hgt"].replace("in", "")) <= 76):
                continue
        if not (re.search("^#([A-Fa-f0-9]{6})$", fields["hcl"])):
            continue
        if not (fields["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            continue
        if not (len(fields["pid"]) == 9):
            continue
        validCount += 1


print(validCount)
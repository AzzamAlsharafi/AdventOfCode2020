import os.path

rules = dict()

gold = "shiny gold"
none = "none"

with open(os.path.join("Day 07", "input.txt")) as f:
    for line in f:
        bag, rule = line.split(" bags contain ")

        if "no other" in rule:
            rule = none
        else:        
            rule = [r.replace(" bags", "").replace(" bag", "") for r in rule.replace("\n", "").replace(".", "").split(", ")]
        
        rules[bag] = rule

def containedBags(bag):
    contained = 1

    if rules[bag] is none:
        return contained

    for b in rules[bag]:
        contained += (int(b[:1]) * containedBags(b[2:]))

    return contained

print(containedBags(gold) - 1)
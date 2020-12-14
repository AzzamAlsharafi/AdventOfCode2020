import os.path

rules = dict()

gold = "shiny gold"
none = "none"

with open(os.path.join("Day 07", "input.txt")) as f:
    for line in f:
        bag, rule = line.split(" bags contain ")

        if "no other" in rule:
            rule = none
        elif gold in rule:
            rule = gold
        else:        
            rule = [r[2:].replace(" bags", "").replace(" bag", "") for r in rule.replace("\n", "").replace(".", "").split(", ")]
        
        rules[bag] = rule

def isGold(bag):
    if rules[bag] == gold:
        return True
    elif rules[bag] == none:
        return False
    else:
        return any([isGold(r) for r in rules[bag]])


counter = 0

for r in rules:
    if isGold(r):
        counter += 1

print(counter)
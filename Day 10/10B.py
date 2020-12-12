import os.path

joltages = [0]

with open(os.path.join("Day 10", "input.txt")) as f:
    for line in f:
        joltages.append(int(line))

joltages.sort()

paths = {}

for i in range(len(joltages)):
    paths[joltages[i]] = [j for j in joltages[i+1:i+4] if j <= joltages[i] + 3]

paths[joltages[-1]] = 1

for j in list(reversed(paths.keys()))[1:]:
    value = sum([paths[p] for p in paths[j]])
    paths[j] = value

print(paths[0])
import os.path

joltages = [0]

with open(os.path.join("Day 10", "input.txt")) as f:
    for line in f:
        joltages.append(int(line))

joltages = sorted(joltages)

joltages.append(joltages[len(joltages) - 1] + 3)

oneDiffs = 0
threeDiffs = 0

for i in range(1, len(joltages)):
    if (joltages[i] - joltages[i-1]) == 1:
        oneDiffs += 1
    else:
        threeDiffs += 1

print(oneDiffs * threeDiffs)
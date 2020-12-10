import os.path

grid = []

with open(os.path.join("Day 3", "input.txt")) as f:
    for line in f:
       grid.append(line.replace("\n", ""))

gridWidth = len(grid[0])

currentColumn = 0

treesHit = 0

for row in grid:
    if row[currentColumn] == "#":
        treesHit += 1
    currentColumn += 3
    if currentColumn >= gridWidth:
        currentColumn -= gridWidth

print(treesHit)
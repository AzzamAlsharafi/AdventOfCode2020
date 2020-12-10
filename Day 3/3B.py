import os.path

grid = []
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

with open(os.path.join("Day 3", "input.txt")) as f:
    for line in f:
       grid.append(line.replace("\n", ""))

gridWidth = len(grid[0])

result = 1

for slope in slopes:
    currentColumn = 0
    treesHit = 0
    for row in grid[::slope[1]]:
        if row[currentColumn] == "#":
            treesHit += 1
        currentColumn += slope[0]
        if currentColumn >= gridWidth:
            currentColumn -= gridWidth
    result *= treesHit

print(result)


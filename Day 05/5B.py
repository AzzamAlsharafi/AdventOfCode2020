# COMPLETE TRASH

import os.path

ids = []

def calculateSeatId(seat):
    global ids
    rows = [1, 128]
    for s in seat[:7]:
        if(s == "F"):
            rows[1] -= ((rows[1] - (rows[0]-1)) / 2)
        else:
            rows[0] += ((rows[1] - (rows[0]-1)) / 2)
    
    columns = [1, 8]
    for s in seat[7:]:
        if(s == "L"):
            columns[1] -= ((columns[1] - (columns[0]-1)) / 2)
        else:
            columns[0] += ((columns[1] - (columns[0]-1)) / 2)

    id = ((rows[0] - 1) * 8) + (columns[0] - 1)

    if id == 6.5 or id == 933.5:
        print(rows[0] - 1, columns[0] - 1)
    
    print("ss", rows[0] - 1, columns[0] - 1)

    return id
    

with open(os.path.join("Day 05", "input.txt")) as f:
    for line in f:
        ids.append(calculateSeatId(line))

print(max(ids))
print(min(ids))
ids = sorted(ids)
print(ids)
for i in range(1, len(ids)):
    if not (ids[i] == ids[i-1] + 1):
        print("dsd", ids[i])

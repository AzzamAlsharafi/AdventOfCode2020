import os.path

ids = []

def calculateSeatId(seat):
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
    return id
    

with open(os.path.join("Day 5", "input.txt")) as f:
    for line in f:
        ids.append(calculateSeatId(line))

print(max(ids))
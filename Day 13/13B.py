import os.path

buses = []

with open(os.path.join("Day 13", "input.txt")) as f:
    f.readline()
    buses = [b for b in f.readline().split(",")]

offsets = [i for i in range(len(buses)) if buses[i] != "x"]

buses = [int(b) for b in buses if b != "x"]

for i in range(len(buses)):
    if offsets[i] > buses[i]:
        offsets[i] = offsets[i] % buses[i]

def offsetsFromTimestamp(t, bs):
    return [b - (t % b) if (t % b) != 0 else 0 for b in bs]

timestamp = -(offsets[buses.index(max(buses[:2]))])
increase = max(buses[:2])

for i in range(2, len(buses) + 1):
    subBuses, subOffsets = buses[:i], offsets[:i] 

    prevMatch = -1

    while True:
        if offsetsFromTimestamp(timestamp, subBuses) == subOffsets:
            if prevMatch == -1:
                prevMatch = timestamp
            else:
                increase = timestamp - prevMatch
                timestamp = prevMatch
                break
        timestamp += increase

print(timestamp)

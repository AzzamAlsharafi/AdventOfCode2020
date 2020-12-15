import os.path

earliest = 0
buses = []

with open(os.path.join("Day 13", "input.txt")) as f:
    earliest = int(f.readline())
    buses = [int(b) for b in f.readline().split(",") if b != "x"]

remaining = [b - (earliest % b) for b in buses]

print(min(remaining) * buses[remaining.index(min(remaining))])

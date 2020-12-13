import os.path
import copy

seats = []

with open(os.path.join("Day 11", "input.txt")) as f:
    for line in f:
        seats.append(list(line.replace("\n", "")))

def updateSeat(row, column, original):
    if original == ".":
        return original

    adjacent = []

    for r in range(-1, 2):
        for c in range(-1, 2):
            if -1 < row + r < len(seats) and -1 < column + c < len(seats[0]) and not (r == 0 and c == 0):
                adjacent.append(seats[row + r][column + c])

    occupied = adjacent.count("#")

    if occupied >= 4:
        return "L"
    elif occupied == 0:
        return "#"
    else:
        return original

def updateAll():
    copySeats = copy.deepcopy(seats)

    for r in range(len(copySeats)):
        for c in range(len(copySeats[0])):
            copySeats[r][c] = updateSeat(r, c, copySeats[r][c])

    return copySeats

prevOccupied = -1

while True:
    seats = updateAll()
    occupied = "".join("".join(r) for r in seats).count("#")
    if occupied == prevOccupied:
        print(occupied)
        break
    prevOccupied = occupied
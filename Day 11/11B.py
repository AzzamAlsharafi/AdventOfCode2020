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
            if not (r == 0 and c == 0):
                nextR = row + r
                nextC = column + c
                while True:
                    if not (-1 < nextR < len(seats) and -1 < nextC < len(seats[0])):
                        break

                    if seats[nextR][nextC] != ".":
                        adjacent.append(seats[nextR][nextC])
                        break
                    nextR += r
                    nextC += c

    occupied = adjacent.count("#")

    if occupied >= 5:
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
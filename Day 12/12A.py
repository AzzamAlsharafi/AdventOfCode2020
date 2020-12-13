import os.path

location = [0, 0]
shipDirection = "E"

directions = ["E", "S", "W", "N"]

def move(direction, value):
    if direction == "N":
        location[1] += value
    elif direction == "S":
        location[1] -= value
    elif direction == "E":
        location[0] += value
    elif direction == "W":
        location[0] -= value

def changeDirection(turn, angle):
    global shipDirection

    value = angle // 90
    if turn == "L":
        value = -value
    
    newIndex = directions.index(shipDirection) + value

    if newIndex > 3:
        newIndex = newIndex - 4

    shipDirection = directions[newIndex]

def runInstruction(instruction):
    action, value = instruction[0:1], int(instruction[1:])
    
    if action in directions:
        move(action, value)
    elif action == "F":
        move(shipDirection, value)
    else:
        changeDirection(action, value)

with open(os.path.join("Day 12", "input.txt")) as f:
    for line in f:
        runInstruction(line)

print(sum(map(abs, location)))
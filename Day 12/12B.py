import os.path

location = [0, 0]
waypoint = [10, 1]

directions = ["E", "S", "W", "N"]

def moveWaypoint(direction, value):
    if direction == "N":
        waypoint[1] += value
    elif direction == "S":
        waypoint[1] -= value
    elif direction == "E":
        waypoint[0] += value
    elif direction == "W":
        waypoint[0] -= value

def moveShip(times):
    location[0] += waypoint[0] * times
    location[1] += waypoint[1] * times
    return 0

def rotateWaypoint(turn):
    waypoint.reverse()
    if turn == "R":
        waypoint[1] = -waypoint[1]
    else:
        waypoint[0] = -waypoint[0]

def changeDirection(turn, angle):
    value = angle // 90
    
    for _ in range(value):
        rotateWaypoint(turn)


def runInstruction(instruction):
    action, value = instruction[0:1], int(instruction[1:])
    
    if action in directions:
        moveWaypoint(action, value)
    elif action == "F":
        moveShip(value)
    else:
        changeDirection(action, value)

with open(os.path.join("Day 12", "input.txt")) as f:
    for line in f:
        runInstruction(line)

print(sum(map(abs, location)))
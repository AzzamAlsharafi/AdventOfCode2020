import os.path

instructions = []
executed = []

with open(os.path.join("Day 08", "input.txt")) as f:
    for line in f:
        instructions.append(line)

def runInstruction(current, accumulator):
    if current in executed:
        return accumulator

    instruction = instructions[current]
    executed.append(current)

    if instruction[:3] == "nop":
        current += 1
    elif instruction[:3] == "acc":
        accumulator += int(instruction[4:])
        current += 1
    else:
        current += int(instruction[4:])
    
    return runInstruction(current, accumulator)

print(runInstruction(0, 0))
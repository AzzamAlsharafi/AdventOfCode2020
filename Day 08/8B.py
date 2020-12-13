import os.path

oInstructions = []
executed = []

with open(os.path.join("Day 8", "input.txt")) as f:
    for line in f:
        oInstructions.append(line)

def runInstruction(current, accumulator, instructions=oInstructions):
    if current >= len(instructions):
        return accumulator

    if current in executed:
        return -1

    instruction = instructions[current]
    executed.append(current)

    if instruction[:3] == "nop":
        current += 1
    elif instruction[:3] == "acc":
        accumulator += int(instruction[4:])
        current += 1
    else:
        current += int(instruction[4:])
    
    return runInstruction(current, accumulator, instructions)

toEdit = -1
newInstructions = oInstructions.copy()

while True:
    result = runInstruction(0, 0, newInstructions)
    if result == -1:
        newInstructions = oInstructions.copy()
        for i in range(len(newInstructions)):
            if ("nop" in newInstructions[i] or "jmp" in newInstructions[i]) and i > toEdit:
                toEdit = i
                break
        
        if "nop" in newInstructions[toEdit]:
            newInstructions[toEdit] = newInstructions[toEdit].replace("nop", "jmp")
        else:
            newInstructions[toEdit] = newInstructions[toEdit].replace("jmp", "nop")

        executed = []
    else:
        print(result)
        break
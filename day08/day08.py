import copy

instructions = {}
num = 0

for instruction in open("day08.txt"):
    num += 1
    instructions[num] = instruction.strip()


def accumulate(instructionsToCheck):
    passedInstructions = []
    counter = 1
    accumulator = 0
    while counter <= len(instructionsToCheck):

        instruction, number = instructionsToCheck[counter].split()[0:2]
        if counter not in passedInstructions:
            passedInstructions.append(counter)
        else:
            return False, accumulator

        if instruction == 'nop':
            counter += 1
        elif instruction == 'acc':
            accumulator += int(number)
            counter += 1
        else:
            counter += int(number)

    return True, accumulator


print("Part 1:", accumulate(instructions)[1])

nextInstruction = 1
while True:
    startInstructions = copy.deepcopy(instructions)

    instruction = startInstructions[nextInstruction].split()[0]
    number = startInstructions[nextInstruction].split()[1]

    if instruction == 'nop' or instruction == 'jmp':
        changeInstruction = 'nop' if instruction == 'jmp' else 'jmp'
        newInstruction = changeInstruction + ' ' + number
        startInstructions[nextInstruction] = newInstruction

    nextInstruction += 1

    success, result = accumulate(startInstructions)
    if success:
        print("Part 2:", result)
        break

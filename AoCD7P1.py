### Advent of Code - Day 7 ###

### Imported Packets
from itertools import permutations

### Opening the file
data = [int(d) for d in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split(",")]

### Defining Subroutines
def getPermutations(myList):
    for permutation in permutations(myList):
        yield permutation

def Instruction(instructionSet):
    return [int(i) for i in [instructionSet[2], instructionSet[1], instructionSet[0], instructionSet[3:]]]

def getParameter(mode, offset, index, data):
    if mode == 0:
        return data[data[index + offset]]
    return data[index + offset]

def Simulate(data, input1, input2):
    index = 0
    inputCheck = False
    while data[index] != 99:
        modeA, modeB, modeC, opcode = Instruction(f"{data[index]:05}")
        if opcode == 1:
            parameter1, parameter2 = getParameter(modeA, 1, index, data), getParameter(modeB, 2, index, data)
            data[data[index + 3]] = parameter1 + parameter2
            index += 4
        elif opcode == 2:
            parameter1, parameter2 = getParameter(modeA, 1, index, data), getParameter(modeB, 2, index, data)
            data[data[index + 3]] = parameter1 * parameter2
            index += 4
        elif opcode == 3:
            if inputCheck == False:
                data[data[index + 1]] = int(input1)
                inputCheck = True
            else:
                data[data[index + 1]] = int(input2)
            index += 2
        elif opcode == 4:
            return data[data[index + 1]]
            index += 2
        elif opcode == 5:
            parameter1, parameter2 = getParameter(modeA, 1, index, data), getParameter(modeB, 2, index, data)
            if parameter1 != 0:
                index = parameter2
            else:
                index += 3
        elif opcode == 6:
            parameter1, parameter2 = getParameter(modeA, 1, index, data), getParameter(modeB, 2, index, data)
            if parameter1 == 0:
                index = parameter2
            else:
                index += 3
        elif opcode == 7:
            parameter1, parameter2 = getParameter(modeA, 1, index, data), getParameter(modeB, 2, index, data)
            if parameter1 < parameter2:
                data[data[index + 3]] = 1
            else:
                data[data[index + 3]] = 0
            index += 4
        elif opcode == 8:
            parameter1, parameter2 = getParameter(modeA, 1, index, data), getParameter(modeB, 2, index, data)
            if parameter1 == parameter2:
                data[data[index + 3]] = 1
            else:
                data[data[index + 3]] = 0
            index += 4
        else:
            raise ValueError("Failed Opcode. ")

def Amplifiers(data):
    Highest = 0
    for signal in getPermutations([0, 1, 2, 3, 4]):
        output = 0
        for inputSignal in signal:
                output = Simulate(data[:], inputSignal, output)
        if output > Highest:
            Highest = output
    return Highest

### Running the Program
print(Amplifiers(data))

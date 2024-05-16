### Advent of Code - Day 5 ###

## Opening the file
data = [int(d) for d in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split(",")]

## Defining Subroutines
def Instruction(instructionSet):
    return [int(i) for i in [instructionSet[2], instructionSet[1], instructionSet[0], instructionSet[3:]]]

def get_parameter(mode, offset, index, data):
    if mode == 0:
        return data[data[index + offset]]
    return data[index + offset]

def Simulate(data):
    index = 0
    while data[index] != 99:
        modeA, modeB, modeC, opcode = Instruction(f"{data[index]:05}")
        if opcode == 1:
            parameter1, parameter2 = get_parameter(modeA, 1, index, data), get_parameter(modeB, 2, index, data)
            data[data[index + 3]] = parameter1 + parameter2
            index += 4
        elif opcode == 2:
            parameter1, parameter2 = get_parameter(modeA, 1, index, data), get_parameter(modeB, 2, index, data)
            data[data[index + 3]] = parameter1 * parameter2
            index += 4
        elif opcode == 3:
            data[data[index + 1]] = int(input())
            index += 2
        elif opcode == 4:
            print(data[data[index + 1]])
            index += 2
        elif opcode == 5:
            parameter1, parameter2 = get_parameter(modeA, 1, index, data), get_parameter(modeB, 2, index, data)
            if parameter1 != 0:
                index = parameter2
            else:
                index += 3
        elif opcode == 6:
            parameter1, parameter2 = get_parameter(modeA, 1, index, data), get_parameter(modeB, 2, index, data)
            if parameter1 == 0:
                index = parameter2
            else:
                index += 3
        elif opcode == 7:
            parameter1, parameter2 = get_parameter(modeA, 1, index, data), get_parameter(modeB, 2, index, data)
            if parameter1 < parameter2:
                data[data[index + 3]] = 1
            else:
                data[data[index + 3]] = 0
            index += 4
        elif opcode == 8:
            parameter1, parameter2 = get_parameter(modeA, 1, index, data), get_parameter(modeB, 2, index, data)
            if parameter1 == parameter2:
                data[data[index + 3]] = 1
            else:
                data[data[index + 3]] = 0
            index += 4
        else:
            print("Failed Opcode. ")

## Running the Program
Simulate(data[:])

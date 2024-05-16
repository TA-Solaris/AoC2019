### Advent of Code - Day 9 ###

## Opening the file
dataRaw = [int(d) for d in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split(",")]

## Defining Subroutines
def FixData(raw, new):
    count = 0
    for x in raw:
        new[count] = x
        count += 1
    for _ in range(count, 500000):
        new[count] = 0
        count += 1
    return new

def Instruction(instructionSet):
    return [int(i) for i in [instructionSet[2], instructionSet[1], instructionSet[0], instructionSet[3:]]]

def getOperand(mode, offset, index, data, relativeBase, ControlValue):
    if ControlValue == "READ":
        if mode == 0:
            return data[data[index + offset]]
        if mode == 1:
            return data[index + offset]
        if mode == 2:
            return data[relativeBase + data[index + offset]]
        else:
            raise ValueError("Invalid mode for operand. ")
    if ControlValue == "WRITE":
        if mode == 0:
            return data[index + offset]
        if mode == 2:
            return (relativeBase + data[index + offset])
        else:
            raise ValueError("Invalid mode for operand. ")
    else:
        raise ValueError("Invalid input from Control Unit. ")

def Simulate(data):
    index = 0
    relativeBase = 0
    CU = "READ"
    while data[index] != 99:
        modeA, modeB, modeC, opcode = Instruction(f"{data[index]:05}")
        if opcode == 1:
            CU = "READ"
            operand1, operand2 = getOperand(modeA, 1, index, data, relativeBase, CU), getOperand(modeB, 2, index, data, relativeBase, CU)
            CU = "WRITE"
            operand3 = getOperand(modeC, 3, index, data, relativeBase, CU)
            data[operand3] = operand1 + operand2
            index += 4
        elif opcode == 2:
            CU = "READ"
            operand1, operand2 = getOperand(modeA, 1, index, data, relativeBase, CU), getOperand(modeB, 2, index, data, relativeBase, CU)
            CU = "WRITE"
            operand3 = getOperand(modeC, 3, index, data, relativeBase, CU)
            data[operand3] = operand1 * operand2
            index += 4
        elif opcode == 3:
            CU = "WRITE"
            operand1 = getOperand(modeA, 1, index, data, relativeBase, CU)
            data[operand1] = int(input("INPUT: "))
            index += 2
        elif opcode == 4:
            CU = "READ"
            operand1 = getOperand(modeA, 1, index, data, relativeBase, CU)
            print("OUTPUT: {}".format(operand1))
            index += 2
        elif opcode == 5:
            CU = "READ"
            operand1, operand2 = getOperand(modeA, 1, index, data, relativeBase, CU), getOperand(modeB, 2, index, data, relativeBase, CU)
            if operand1 != 0:
                index = operand2
            else:
                index += 3
        elif opcode == 6:
            CU = "READ"
            operand1, operand2 = getOperand(modeA, 1, index, data, relativeBase, CU), getOperand(modeB, 2, index, data, relativeBase, CU)
            if operand1 == 0:
                index = operand2
            else:
                index += 3
        elif opcode == 7:
            CU = "READ"
            operand1, operand2 = getOperand(modeA, 1, index, data, relativeBase, CU), getOperand(modeB, 2, index, data, relativeBase, CU)
            CU = "WRITE"
            operand3 = getOperand(modeC, 3, index, data, relativeBase, CU)
            if operand1 < operand2:
                data[operand3] = 1
            else:
                data[operand3] = 0
            index += 4
        elif opcode == 8:
            CU = "READ"
            operand1, operand2 = getOperand(modeA, 1, index, data, relativeBase, CU), getOperand(modeB, 2, index, data, relativeBase, CU)
            CU = "WRITE"
            operand3 = getOperand(modeC, 3, index, data, relativeBase, CU)
            if operand1 == operand2:
                data[operand3] = 1
            else:
                data[operand3] = 0
            index += 4
        elif opcode == 9:
            CU = "READ"
            operand1 = getOperand(modeA, 1, index, data, relativeBase, CU)
            relativeBase += operand1
            index += 2
        else:
            print("Failed Opcode. ")

### Turning the data into a dictionary
data = {}
data = FixData(dataRaw, data)

### Running the Program
Simulate(data)

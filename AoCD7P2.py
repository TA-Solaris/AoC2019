### Advent of Code - Day 7 ###

### Imported Packets
from itertools import permutations

### Opening the file
data = [int(d) for d in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split(",")]

### Defining Functions
def getPermutations(myList):
    for permutation in permutations(myList):
        yield permutation

def Instruction(instructionSet):
    return [int(i) for i in [instructionSet[2], instructionSet[1], instructionSet[0], instructionSet[3:]]]

### Defining Classes
class IntcodeMachine:
    def __init__(self, data):
        self.index = 0
        self.data = data
        self.done = False
        self.output = None
        self.inputs = []

    def getParameter(self, mode, offset):
        if mode == 0:
            return self.data[self.data[self.index + offset]]
        return self.data[self.index + offset]

    def calculate(self, input_val):
        self.inputs.append(input_val)
        while True:
            modeA, modeB, modeC, opcode = Instruction(f"{self.data[self.index]:05}")
            if opcode == 1:
                parameter1, parameter2 = self.getParameter(modeA, 1), self.getParameter(modeB, 2)
                self.data[self.data[self.index + 3]] = parameter1 + parameter2
                self.index += 4
            elif opcode == 2:
                parameter1, parameter2 = self.getParameter(modeA, 1), self.getParameter(modeB, 2)
                self.data[self.data[self.index + 3]] = parameter1 * parameter2
                self.index += 4
            elif opcode == 3:
                self.data[self.data[self.index + 1]] = self.inputs.pop(0)
                self.index += 2
            elif opcode == 4:
                self.output = self.data[self.data[self.index + 1]]
                self.index += 2
                return self.output
            elif opcode == 5:
                parameter1, parameter2 = self.getParameter(modeA, 1), self.getParameter(modeB, 2)
                if parameter1 != 0:
                    self.index = parameter2
                else:
                    self.index += 3
            elif opcode == 6:
                parameter1, parameter2 = self.getParameter(modeA, 1), self.getParameter(modeB, 2)
                if parameter1 == 0:
                    self.index = parameter2
                else:
                    self.index += 3
            elif opcode == 7:
                parameter1, parameter2 = self.getParameter(modeA, 1), self.getParameter(modeB, 2)
                if parameter1 < parameter2:
                    self.data[self.data[self.index + 3]] = 1
                else:
                    self.data[self.data[self.index + 3]] = 0
                self.index += 4
            elif opcode == 8:
                parameter1, parameter2 = self.getParameter(modeA, 1), self.getParameter(modeB, 2)
                if parameter1 == parameter2:
                    self.data[self.data[self.index + 3]] = 1
                else:
                    self.data[self.data[self.index + 3]] = 0
                self.index += 4
            elif opcode == 99:
                self.done = True
                return self.output

### Running the program
lastOutput = 0
for permutation in getPermutations([5, 6, 7, 8, 9]):
    amplifiers = [IntcodeMachine(data[:]) for _ in range(5)]
    outputSignal = 0
    for amplifier, phases in zip(amplifiers, permutation):
        amplifier.inputs.append(phases)
    while amplifiers[4].done == False:
        for amplifier in amplifiers:
            outputSignal = amplifier.calculate(outputSignal)
    lastOutput = max(outputSignal, lastOutput)
print(lastOutput)

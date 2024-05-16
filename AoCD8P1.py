### Advent of Code - Day 8 ###

### Constants
HEIGHT = 6
WIDTH = 25

### Opening the file
data = [int(d) for d in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read()]

### Defining Subroutines
def getLayers(width, height, data):
    count = 0
    while count < len(data):
        yield data[count:count + (width * height)]
        count += width * height

def Least(number, myList):
    minimum = min([i.count(number) for i in myList])
    for layer in myList:
        if layer.count(number) == minimum:
            return myList.index(layer)

### Filling a list lists representing the layers
Layers = [layer for layer in getLayers(WIDTH, HEIGHT, data)]

### Analysis
LeastZeros = Least(0, Layers)

### Outputting
print(Layers[LeastZeros].count(1) * Layers[LeastZeros].count(2))

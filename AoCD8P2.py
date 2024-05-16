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

def getPixels(width, height, layers, endList):
    for pixel in range(0, width * height):
        layer = 0
        while True:
            if layers[layer][pixel] == 2:
                layer += 1
            elif layers[layer][pixel] == 1:
                endList.append(1)
                break
            elif layers[layer][pixel] == 0:
                endList.append(0)
                break
    return endList
        

### Filling a list lists representing the layers
Layers = [layer for layer in getLayers(WIDTH, HEIGHT, data)]

### Creating a list of the decoded pixels
pixels = []
pixels = getPixels(WIDTH, HEIGHT, Layers, pixels)

### Outputting
count = 0
for pixel in pixels:
    if pixel == 1:
        print("X", end = "")
    elif pixel == 0:
        print("-", end = "")
    count += 1
    if count % WIDTH == 0:
        print("")

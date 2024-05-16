### Advent of Code - Day 10 ###

### Imports
import math

### Opening the file
board = [list(d) for d in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split("\n")]

### Counting the size of the board
HEIGHT = len(board)
WIDTH = len(board[0])

### Getting all the asteroid co-ords
coords = []
for y in range(HEIGHT):
    for x in range(WIDTH):
        if board[y][x] == "#":
            coords.append((x, y))

### Creating a list for the number of asteroids an asteroid can see
number = [0] * len(coords)

### Doing some calculations and things I guess
index = 0
for base in coords:
    angles = []
    for other in coords:
        if other != base:
            if base[0] < other[0]:
                # Asteroid to the right
                if base[1] < other[1]:
                    # Asteroid to the right and up
                    angle = math.atan2(other[0] - base[0], base[1] - other[1])
                    angle = math.degrees(angle)
                elif base[1] > other[1]:
                    # Asteroid to the right and down
                    angle = math.atan2(other[1] - base[1], other[0] - base[0])
                    angle = math.degrees(angle) + 90
                else:
                    # Asteroid to the right
                    angle = 90
            elif base[0] > other[0]:
                # Asteroid to the left
                if base[1] < other[1]:
                    # Asteroid to the left and up
                    angle = math.atan2(base[1] - other[1], base[0] - other[0])
                    angle = math.degrees(angle) + 270
                elif base[1] > other[1]:
                    # Asteroid to the left and down
                    angle = math.atan2(base[0] - other[0], other[1] - base[1])
                    angle = math.degrees(angle) + 180
                else:
                    # Asteroid to the left
                    angle = 270
            else:
                if base[1] > other[1]:
                    # Asteroid up
                    angle = 0
                else:
                    # Asteroid down
                    angle = 180
            if angle not in angles:
                angles.append(angle)
                number[index] += 1
    index += 1

### Part 2
base = coords[number.index(max(number))]
anglesDict = {}
angles = []
numberCounter = 0
for other in coords:
    if other != base:
        if base[0] < other[0]:
            # Asteroid to the right
            if base[1] < other[1]:
                # Asteroid to the right and up
                angle = math.atan2(other[0] - base[0], base[1] - other[1])
                angle = math.degrees(angle)
            elif base[1] > other[1]:
                # Asteroid to the right and down
                angle = math.atan2(other[1] - base[1], other[0] - base[0])
                angle = math.degrees(angle) + 90
            else:
                # Asteroid to the right
                angle = 90
        elif base[0] > other[0]:
            # Asteroid to the left
            if base[1] < other[1]:
                # Asteroid to the left and up
                angle = math.atan2(base[1] - other[1], base[0] - other[0])
                angle = math.degrees(angle) + 270
            elif base[1] > other[1]:
                # Asteroid to the left and down
                angle = math.atan2(base[0] - other[0], other[1] - base[1])
                angle = math.degrees(angle) + 180
            else:
                # Asteroid to the left
                angle = 270
        else:
            if base[1] > other[1]:
                # Asteroid up
                angle = 0
            else:
                # Asteroid down
                angle = 180
        if angle not in angles:
            anglesDict[angle] = other
            angles.append(angle)
            numberCounter += 1

### Outputting
angles.sort()
angleBest = angles[198]
print(angleBest)

print(anglesDict[angleBest])

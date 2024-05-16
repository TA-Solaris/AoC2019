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
for asteroid in coords:
    gradients = []
    for other in coords:
        direction = "left"
        if other != asteroid:
            if asteroid[0] <= other[0]:
                direction = "right"
                try:
                    gradient = (other[1] - asteroid[1]) / (other[0] - asteroid[0])
                except ZeroDivisionError:
                    if asteroid[1] <= other[1]:
                        direction = "up"
                    else:
                        direction = "down"
                    gradient = "hi broken maths"
            else:
                direction = "left"
                gradient = (other[1] - asteroid[1]) / (other[0] - asteroid[0])
            if (gradient, direction) not in gradients:
                gradients.append((gradient, direction))
                number[index] += 1
    index += 1

### Outputting
print(coords[number.index(max(number))])
print(max(number))

### IMMA HEAD OUT NOW

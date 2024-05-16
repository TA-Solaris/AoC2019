### Advent of Code - Day 3 ###

### Inputting
wire1, wire2 = open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split("\n")
wire1 = wire1.split(",")
wire2 = wire2.split(",")

### Defining Subroutines
def GetCoords(directions):
	## Dictionary to store the values of the coords the robot travels
	allCoords = {}

	## To store the current position of the robot
	x = 0
	y = 0

	## Counter for part two
	step = 0

	## Simulating
	for move in directions:
		direction = move[0]
		distance = int(move[1:])

		xdir = 0
		ydir = 0
		if direction == "L":
			xdir = -1
		elif direction == "R":
			xdir = 1
		elif direction == "D":
			ydir = -1
		elif direction == "U":
			ydir = 1
		else:
			raise ValueError("Incorrect Direction")
		
		for _ in range(0, distance):
			x += xdir
			y += ydir
			step += 1

			## Important for no repeated intersections
			if (x,y) not in allCoords:
				allCoords[(x,y)] = step
	return allCoords

### Running the Program

## Getting all coord positions
wire1 = GetCoords(wire1)
wire2 = GetCoords(wire2)

## Getting Intersections
intersections = list(set(wire1.keys()) & set(wire2.keys()))

### Analysing the wires

## Part 1
distances = [abs(intersection[0]) + abs(intersection[1]) for intersection in intersections]
minDistance = min(distances)

## Part 2
totalSteps = [wire1[i] + wire2[i] for i in intersections]
minSteps = min(totalSteps)

### Outputting
print("Part 1: {}".format(minDistance))
print("Part 2: {}".format(minSteps))

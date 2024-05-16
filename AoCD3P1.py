### Advent of Code - Day 3 ###

####### THIS IS INCREADIBLY BUT FUN OK

## Inputting
wire1, wire2 = open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split("\n")
wire1 = wire1.split(",")
wire2 = wire2.split(",")
print("Import Sucessful. ")

## Defining Classes
class Stack:
	def __init__(self):
		self.head = None
	
	def isEmpty(self):
		return self.head == None
	
	def isFull(self):
		return False ## (Never full unless out of memory)
		
	def push(self, item):
		if self.isFull() == False:
			newItem = StackItem(item)
			newItem.setNext(self.head)
			self.head = newItem
		else:
			raise MemoryError()
	
	def pop(self):
		if self.isEmpty() == False:
			value = self.head.item
			self.head = self.head.next
			return value
		else:
			print("Error: The stack is empty. ")
	
	def peek(self):
		if self.isEmpty() == False:
			return self.head.item
		else:
			print("Error: The stack is empty. ")

class StackItem:
	def __init__(self, item):
		self.item = item
		self.next = None
	
	def setNext(self, next):
		self.next = next

## Creating an instance of the class
myStackWire1 = Stack()
myStackWire2 = Stack()

## Adding StartPositions
myStackWire1.push([0, 0])
myStackWire2.push([0, 0])

## Creating Lists
myListWire1 = [(0,0)]
myListWire2 = [(0,0)]
intersections = []

## Adding Co-ord Positions
for code in wire1:
	if code[0] == "R":
		for x in range(myStackWire1.peek()[0], myStackWire1.peek()[0] + int(code[1:]) + 1):
			y = myStackWire1.peek()[1]
			myListWire1.append((x, y))
		myStackWire1.push([myStackWire1.peek()[0] + int(code[1:]), myStackWire1.peek()[1]])
	elif code[0] == "L":
		for x in range(myStackWire1.peek()[0], myStackWire1.peek()[0] - int(code[1:]) - 1, -1):
			y = myStackWire1.peek()[1]
			myListWire1.append((x, y))
		myStackWire1.push([myStackWire1.peek()[0] - int(code[1:]), myStackWire1.peek()[1]])
	elif code[0] == "U":
		for y in range(myStackWire1.peek()[1], myStackWire1.peek()[1] + int(code[1:]) + 1):
			x = myStackWire1.peek()[0]
			myListWire1.append((x, y))
		myStackWire1.push([myStackWire1.peek()[0], myStackWire1.peek()[1] + int(code[1:])])
	elif code[0] == "D":
		for y in range(myStackWire1.peek()[1], myStackWire1.peek()[1] - int(code[1:]) - 1, -1):
			x = myStackWire1.peek()[0]
			myListWire1.append((x, y))
		myStackWire1.push([myStackWire1.peek()[0], myStackWire1.peek()[1] - int(code[1:])])

for code in wire2:
	if code[0] == "R":
		for x in range(myStackWire2.peek()[0], myStackWire2.peek()[0] + int(code[1:]) + 1):
			y = myStackWire2.peek()[1]
			myListWire2.append((x, y))
		myStackWire2.push([myStackWire2.peek()[0] + int(code[1:]), myStackWire2.peek()[1]])
	elif code[0] == "L":
		for x in range(myStackWire2.peek()[0], myStackWire2.peek()[0] - int(code[1:]) - 1, -1):
			y = myStackWire2.peek()[1]
			myListWire2.append((x, y))
		myStackWire2.push([myStackWire2.peek()[0] - int(code[1:]), myStackWire2.peek()[1]])
	elif code[0] == "U":
		for y in range(myStackWire2.peek()[1], myStackWire2.peek()[1] + int(code[1:]) + 1):
			x = myStackWire2.peek()[0]
			myListWire2.append((x, y))
		myStackWire2.push([myStackWire2.peek()[0], myStackWire2.peek()[1] + int(code[1:])])
	elif code[0] == "D":
		for y in range(myStackWire2.peek()[1], myStackWire2.peek()[1] - int(code[1:]) - 1, -1):
			x = myStackWire2.peek()[0]
			myListWire2.append((x, y))
		myStackWire2.push([myStackWire2.peek()[0], myStackWire2.peek()[1] - int(code[1:])])

print("Co-ordinates Analyzed. ")

## Finding intersections
num = 0

for pos in myListWire1:
	num += 1
	if (num % 1000) == 1:
		print("Loading: {}%".format(((num/len(myListWire1)*100) // 0.001)*0.001))
	if pos in myListWire2:
		intersections.append(pos)

print("Intersections Found. ")

## Finding the closest one
closest = (5000000, 5000000)
closestdistance = 10000000

for pos in intersections:
	x, y = pos
	if x != 0 and y != 0:
		if x < 0:
			x = -x
		if y < 0:
			y = -y
		if (x+y) <= closestdistance:
			closest = pos
			closestdistance = x + y

## Outputting
print("Closest Found.")
print(closest)
print(closestdistance)

### Advent of Code - Day 2 ###

## Opening the file
intcode = [int(i) for i in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split(",")]

## Do the strange thing
intcode[1] = 12
intcode[2] = 2

## Doing the loop ting
count = 0
while True:
    if intcode[count] == 1:
        intcode[intcode[count + 3]] = intcode[intcode[count + 1]] + intcode[intcode[count + 2]]
    elif intcode[count] == 2:
        intcode[intcode[count + 3]] = intcode[intcode[count + 1]] * intcode[intcode[count + 2]]
    elif intcode[count] == 99:
        break
    count += 4

print(intcode[0])

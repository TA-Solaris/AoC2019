### Advent of Code - Day 1 ###

## Opening the file
masses = open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split("\n")

## Doing the loop ting
total = 0
for x in masses:
    fuel = 1
    fueltotal = 0
    x = int(x)
    while fuel > 0:
        fuel = max((x // 3 - 2), 0)
        x = fuel
        fueltotal += fuel
    total += fueltotal

print(total)

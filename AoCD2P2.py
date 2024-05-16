### Advent of Code - Day 2 ###

## Do the strange thing
for x in range(100):
    for y in range(100):
        ## Opening the file
        intcode = [int(i) for i in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split(",")]

        intcode[1] = x
        intcode[2] = y

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
        
        if intcode[0] == 19690720:
            noun = x
            verb = y

print((100 * noun) + verb)

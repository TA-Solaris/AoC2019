### Advent of Code - Day 4 ###

### Inputting
low = 136760
high = 595730

### Variable Declaration and Initialisation
count = 0

### Calculating
for x in range(low, high + 1):
    strx = str(x)
    if int(strx[0]) <= int(strx[1]) and int(strx[1]) <= int(strx[2]) and int(strx[2]) <= int(strx[3]) and int(strx[3]) <= int(strx[4]) and int(strx[4]) <= int(strx[5]):
        if int(strx[0]) == int(strx[1]) or int(strx[1]) == int(strx[2]) or int(strx[2]) == int(strx[3]) or int(strx[3]) == int(strx[4]) or int(strx[4]) == int(strx[5]):
            count += 1

### Outputting
print(count)

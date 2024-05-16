### Advent of Code - Day 6 ###

### Opening the file
data = [str(d) for d in open("C:\\Users\\potte\\OneDrive - The Perse School\\Visual Studio Code\\Personal\\AdventOfCode\\Test", "r").read().split("\n")]

### Defining Subroutines
def SplitLine(data):
    center = data.find(")")
    return [str(i) for i in [data[:center], data[(center + 1):]]]

def Fill(data, dictionary, objects):
    for line in data:
        Parent, Child = SplitLine(line)
        dictionary[Child] = Parent
        objects.add(Parent)
        objects.add(Child)
    return dictionary, objects

def getOrbit(current, orbits):
    if current not in orbits: return []
    return [orbits[current]] + getOrbit(orbits[current], orbits)

def DirectAndIndirect(orbits, objects):
    return sum(len(getOrbit(obj, orbits)) for obj in objects)

def Transfer(PointA, PointB, orbits):
    PathA = getOrbit(PointA, orbits)
    PathB = getOrbit(PointB, orbits)
    SharedPoint = [i for i in PathA if i in PathB][0] ## Only want the first one (there will be many)
    OrbitalTransfers = PathA.index(SharedPoint) + PathB.index(SharedPoint)
    return OrbitalTransfers

def Simulate(data):
    Orbits = {}
    Objects = set()
    Orbits, Objects = Fill(data, Orbits, Objects)
    return DirectAndIndirect(Orbits, Objects), Transfer("YOU", "SAN", Orbits)

### Outputting
part1, part2 = Simulate(data)
print("Part 1: {}".format(part1))
print("Part 2: {}".format(part2))

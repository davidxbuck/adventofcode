# Advent of Code 2018 Day 8

# Read file and extract tree

def next_level():
    global inputEOF, level, tree, metasum
    level += 1

    try:
        children = next(inp)
        metadata = next(inp)
    except StopIteration:
        inputEOF = True
        return

    while children > 0:
        children -= 1
        next_level()

    level -= 1
    if metadata > 0:
        metasum += sum([next(inp) for _ in range(metadata)])


inputEOF = False
tree = []
level = 0
metasum = 0

file = open("Advent8.txt", 'r')
inp = map(int, file.read().split())
# inp = iter([2,0,3,0,0,0,1,0,0,1,8,1,0,0,0,2,3,0,0,1,0,0,0,8,8,8])


next_level()

print("Part1: Sum of all metadata:", metasum)

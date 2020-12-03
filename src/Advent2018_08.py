# Advent of Code 2018 Day 8

# Read file and extract tree

from collections import defaultdict


def next_level():
    global inputEOF, level, tree, metasum, node, metadata
    level += 1
    node += 1
    me = node

    try:
        childrencount = next(inp)
        metadatacount = next(inp)
    except StopIteration:
        inputEOF = True
        return

    children[me].append(childrencount)
    metadata[me].append(metadatacount)
    while childrencount > 0:
        childrencount -= 1
        childno = next_level()
        children[me].append(childno)

    level -= 1

    childsum = 0

    if metadatacount > 0:
        for _ in range(metadatacount):
            metadatum = next(inp)
            metasum += metadatum
            childsum += metadatum
            metadata[me].append(metadatum)

    return me


file = open("../inputs2018/Advent8", 'r')
inp = map(int, file.read().split())
# inp = iter([2,1,3,0,0,0,1,0,0,1,8,1,1,0,1,0,9,2,3,0,0,1,0,0,0,8,8,8,2]) # Test neighbours
# inp = iter([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])

inputEOF = False
tree = []
level = 0
metasum = 0
node = 0
metadata = defaultdict(list)
children = defaultdict(list)
parent = 0

next_level()

print("Part1: Sum of all metadata:", metasum)

# Populated dictionaries are:
# Children: for each node(key), first entry is number of children, subsequent entries are node numbers of children
# Metadata: for each node(key), first entry is number of metadata, subsequent entries are metadata for this node
# Outdata:  for each node(key), first entry is True/False whether node value calculated, value is second entry

# Initialise node summary and calculate value of childless nodes, and those whose metadata does not refer to children

print(children)
print(metadata)
outdata = defaultdict(list)
for k, v in children.items():
    if v[0] == 0:
        outdata[k].append(True)
        outdata[k].append(sum(metadata[k][1:]))
    else:
        outdata[k].append(False)
        outdata[k].append(None)

    if v[0] > 0:
        metaflag = True
        for meta in metadata[k][1:]:
            if meta <= v[0]:
                metaflag = False  # Flag will be false if at least one metadata refers to a child node
                break
        if metaflag:
            outdata[k][0] = True
            outdata[k][1] = 0  # If metadata does not refer to children, value of node zero

# Iterate over dictionary until all node values have been calculated

complete = 0

while complete < len(children):

    complete = 0
    for k, v in children.items():  # for all nodes
        if outdata[k][0]:  # tick if outdata already calculated
            complete += 1
            continue

        metasum = 0
        metaflag = True
        for meta in metadata[k][1:]:  # for incomplete nodes, tick over metadata (at least one will refer to a child)
            if meta <= v[0]:  # if meta <= number of children of node k
                if outdata[v[meta]][0]:  # if node calculated for child(meta)
                    metasum += outdata[v[meta]][1]
                else:  # child node not calculated yet
                    metaflag = False

        if metaflag:
            outdata[k][0] = True
            outdata[k][1] = metasum
            complete += 1

print("Part2: Total value of root node:", outdata[1][1])

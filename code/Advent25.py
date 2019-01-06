# Advent of Code 2018 Day 25
#

# Read file and extract stars

file = open("../inputs/Advent25", 'r')
stars = [list(map(int, row.strip().split(","))) for row in file]
neighbours = []

# Calculate Manhattan distances and create sets of neighbours

for ix, star in enumerate(stars):
    # starlist = [ix]
    # for index, calc in enumerate(stars):
    #     if calc != star and sum([abs(calc[x] - star[x]) for x in range(4)]) <= 3:
    #         starlist.append(index)
    # neighbours.append(set(starlist))
    starlist = []
    for index, calc in enumerate(stars):
        if sum([abs(calc[x] - star[x]) for x in range(4)]) <= 3:
            starlist.append(index)
    neighbours.append(set(starlist))

# Merge neighbouring sets into constellations

oldlen = len(neighbours) + 1
while len(neighbours) < oldlen:
    oldlen = len(neighbours)
    for i in range(len(neighbours)):
        for j in range(i + 1, len(neighbours)):
            if len(neighbours[i] & neighbours[j]):
                neighbours[i] = neighbours[i] | neighbours[j]
                neighbours[j] = set()
    neighbours = [neighbours[i] for i in range(len(neighbours)) if neighbours[i] != set()]

print("Part 1 - Total number of constellations:", len(neighbours))

# Advent of Code 2018 Day 6

file = open("../inputs/Advent6", 'r')
input_list = [row for row in file]
inputs = []

# Extract X, Y coordinates from inputs
for row in input_list:
    x, y = row.split(", ")
    inputs.append([int(x), int(y)])
gridmax = int(max(max(inputs)))

# initialise square grid to zeroes

grid = [[0 for i in range(gridmax)] for j in range(gridmax)]

# distcount - number of squares in grid with distcount(index) as nearest point
distcount = [0 for i in range(len(inputs))]

# count of squares with total distance to all points of < 10000
regcount = 0

# for every point in the grid, find distances to all points and therefore:
#    nearest point (if unique)
#    sum of distances to all points

for b in range(gridmax):
    for a in range(gridmax):
        dists = []
        for x, y in inputs:
            dists.append(abs(x-a) + abs(y-b))
        mindist = min(dists)
        if dists.count(mindist) == 1:
            grid[a][b] = str(dists.index(mindist))
            distcount[dists.index(mindist)] += 1
        else:
            grid[a][b] = "."
        if sum(dists) < 10000: regcount += 1

# Eliminate infinites

for z in range(gridmax):

    if grid[0][z] != ".": distcount[int(grid[0][z])] = 0
    if grid[gridmax-1][z] != ".": distcount[int(grid[gridmax-1][z])] = 0
    if grid[z][0] != ".": distcount[int(grid[z][0])] = 0
    if grid[z][gridmax-1] != ".": distcount[int(grid[z][gridmax-1])] = 0

print("Part1: Largest area (excluding infinites):", max(distcount))
print("Part2: Number of coordinates within a combined distance of 10000:", regcount)







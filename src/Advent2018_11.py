# Advent of Code 2018 Day 11
#
# Read file and extract dependencies

file = open("../inputs2018/Advent11", 'r')
serial = int(file.read())
print("Grid serial number:", serial)

import numpy as np

grid_size = 300

# serial = 18

grid = np.zeros((grid_size + 1, grid_size + 1), dtype=int)

# Populate grid with power levels
for x in range(1, grid_size + 1):
    rack_id = x + 10
    for y in range(1, grid_size +1):
        grid[x, y] = (((rack_id * y + serial) * rack_id) % 1000 // 100) - 5

maxpower = -10
for x in range(1, grid_size -1):
    for y in range(1, grid_size -1):
        squarepower = sum(sum(grid[x:x + 3, y:y + 3]))
        if squarepower > maxpower:
            maxpower = squarepower
            maxsquare = "({},{})".format(x, y)

print("Step 1 - Max power is:", maxpower, "in square", maxsquare)


# Brute force method for now. May come back to try the Summed Area Table later
# https://en.wikipedia.org/wiki/Summed-area_table

maxpower = -10000
for squaresize in range(1, grid_size + 1):
    for x in range(1, grid_size +2 -squaresize):
        for y in range(1, grid_size +2 -squaresize):
            squarepower = sum(sum(grid[x:x + squaresize, y:y + squaresize]))
            if squarepower > maxpower:
                maxpower = squarepower
                maxsquare = "({},{},{})".format(x, y, squaresize)

print("Step 2 - Max power is:", maxpower, "in square", maxsquare)

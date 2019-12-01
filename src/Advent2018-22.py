# Advent of Code 2018 Day 22


import re

import numpy as np

MODULO = 20183
C_X = 16807
C_Y = 48271

# Read file and extract values

inp = open("../inputs/Advent22", 'r').read().strip()
depth, targetx, targety = list(map(int, re.search("depth: (\d+)\ntarget: (\d+),(\d+)", inp).group(1,2,3)))
maxx = targetx + 1
maxy = targety + 1

print("Input Depth: {}, Target Coordinates: ({}, {})".format(depth, targetx, targety))

geologic = np.empty((maxx, maxy), dtype=int)
erosion = np.empty((maxx, maxy), dtype=int)
cave_type = np.empty((maxx, maxy), dtype=int)

def populate_grid(x, y):

# The region at 0,0 (the mouth of the cave) has a geologic index of 0
# The region at the coordinates of the target has a geologic index of 0

    if (x == 0 and y == 0) or (x == targetx and y == targety):
        return 0

# If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.

    if y == 0:
        return x * C_X

# If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.

    if x == 0:
        return y * C_Y

# Otherwise, the region's geologic index is the result of multiplying
#     the erosion levels of the regions at X-1,Y and X,Y-1

    return erosion[x-1, y] * erosion[x, y-1]

for (x, y), value in np.ndenumerate(erosion):
    geologic[x, y] = populate_grid(x, y)
    erosion[x, y] = (geologic[x, y] + depth) % MODULO
    cave_type[x, y] = erosion[x, y] % 3


print("Part 1: ", np.sum(cave_type[:targetx+1, :targety+1]))



# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/3
import numpy as np

entries = [list(map(int, row.strip().split())) for row in open('../inputs/Advent2016_03.txt', 'r')]
print(sum(x[0] < x[1] + x[2] and x[1] < x[0] + x[2] and x[2] < x[0] + x[1] for x in entries))

triangles = np.array(entries).transpose()
triangles = triangles.reshape(triangles.size//3, 3)
print(sum(x[0] < x[1] + x[2] and x[1] < x[0] + x[2] and x[2] < x[0] + x[1] for x in triangles))

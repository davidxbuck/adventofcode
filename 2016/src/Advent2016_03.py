# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/3
import numpy as np

triangles = np.array([list(map(int, row.strip().split())) for row in open('../inputs/Advent2016_03.txt', 'r')])
print('AoC 2016 Day 3, Part 1 answer is ', sum(x[0] < x[1] + x[2] and x[1] < x[0] + x[2] and x[2] < x[0] + x[1] for x in triangles))

triangles = triangles.transpose()
triangles = triangles.reshape(triangles.size//3, 3)
print('AoC 2016 Day 3, Part 2 answer is ', sum(x[0] < x[1] + x[2] and x[1] < x[0] + x[2] and x[2] < x[0] + x[1] for x in triangles))

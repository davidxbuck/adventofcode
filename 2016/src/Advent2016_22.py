# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/22
import re
import numpy as np

reg = r"""^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)\%$"""
nodes = [list(map(int, x[0])) for x in
         [re.findall(reg, row.strip()) for row in open('../inputs/Advent2016_22.txt', 'r')][2:]]
x, y = nodes[-1][:2]
used_array = np.empty(shape=(x + 1, y + 1), dtype=int)
free_array = np.empty(shape=(x + 1, y + 1), dtype=int)

for x, y, *node in nodes:
    used_array[x, y] = node[1]
    free_array[x, y] = node[2]

viable = 0
for a in range(x + 1):
    for b in range(y + 1):
        if used_array[a, b] > 0:
            free = free_array >= used_array[a, b]
            free[a, b] = False
            viable += np.sum(free)

print(f"AoC 2016 Day 22, Part 1 answer is {viable}")

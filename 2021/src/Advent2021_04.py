# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/4
#
import numpy as np

data = [x.split('\n') for x in open(f'../inputs/Advent2021_04.txt', 'r').read().split('\n\n')]
balls = list(map(int, data[0][0].split(',')))
grids = np.array([np.loadtxt(data[grid], dtype=int) for grid in range(1, len(data))])

found = set()
for ball in balls:
    grids[grids == ball] = -1
    for ix, grid in enumerate(grids):
        if -5 in np.sum(grid, axis=0) or -5 in np.sum(grid, axis=1):
            found.add(ix)
            if len(found) == 1 or len(found) == len(grids):
                gridcopy = grid.copy()
                gridcopy[gridcopy == -1] = 0
                if len(found) == 1:
                    print(f'Day 4, Part 1 {ball * np.sum(gridcopy)}')
                else:
                    print(f'Day 4, Part 2 {ball * np.sum(gridcopy)}')
                grid[grid == -1] = -10
                break
    if len(found) == len(grids):
        break

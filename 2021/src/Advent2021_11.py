# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/11
#
import numpy as np

inputs = np.array([list(map(int, list(row.strip()))) for row in open("../inputs/Advent2021_11.txt", "r")])
grid = np.zeros(np.array(inputs.shape) + 2, dtype=int)
grid.fill(-999999)
grid[1:inputs.shape[0] + 1, 1:inputs.shape[1] + 1] = inputs

flashes = 0

for loop in range(1, 3000):
    not_flashed = np.ones(grid.shape, dtype=bool)
    grid = grid + 1
    while np.any(grid[not_flashed] > 9):
        for x in range(1, grid.shape[1] - 1):
            for y in range(1, grid.shape[0] - 1):
                if not_flashed[x, y] and grid[x, y] > 9:
                    grid[x - 1: x + 2, y - 1: y + 2] += 1
                    not_flashed[x, y] = False
                    flashes += 1
    grid[grid > 9] = 0
    if loop == 100:
        print(f'Day 11, Part 1 {flashes}')
    if np.sum(not_flashed[1:inputs.shape[0] + 1, 1:inputs.shape[1] + 1]) == 0:
        print(f'Day 11, Part 2 {loop}')
        break

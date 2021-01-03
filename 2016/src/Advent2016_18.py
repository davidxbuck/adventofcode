# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/18


import numpy as np

data = [row.strip() for row in open(f'../inputs/Advent2016_18.txt', 'r')][0]


def mapper(length):
    grid = np.full((length, len(data) + 2), '.')
    grid[0, 1:len(data) + 1] = np.array(list(data))
    for x in range(1, length):
        for y in range(1, len(data) + 1):
            if "".join(grid[x - 1, y - 1:y + 2].tolist()) in ['..^', '.^^', '^^.', '^..']:
                grid[x, y] = '^'
    return np.count_nonzero(grid[0:length, 1:len(data) + 1] == '.')


print(f"AoC 2016 Day 18 Part 1 answer is: {mapper(40)}")
print(f"AoC 2016 Day 18 Part 2 answer is: {mapper(400000)}")

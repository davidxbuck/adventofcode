# Advent of Code 2017
#
# From https://adventofcode.com/2017/day/3
#

from math import sqrt, ceil

import numpy as np


def part1(inp):
    side = ceil(sqrt(inp)) + (1 - ceil(sqrt(inp)) % 2) - 1
    inp -= (side - 1) ** 2
    x = side // 2
    y = side // 2 - min([(inp % side), (side - inp % side)])
    return x + y

def part2(inp):
    grid = np.zeros([100, 100])
    rel = 10
    x = 1
    y = 0
    moves = np.array([1, 2, 2, 3])
    grid[rel, rel] = 1
    grid[rel, rel + 1] = 1

    while True:
        for i, move in enumerate(moves):
            for j in range(move):
                if i == 0:
                    y -= 1
                elif i == 1:
                    x -= 1
                elif i == 2:
                    y += 1
                else:
                    x += 1
                adjacents = np.sum(grid[rel + y - 1:rel + y + 2, rel + x - 1:rel + x + 2])
                grid[rel + y, rel + x] = adjacents
                if adjacents > inp:
                    return adjacents
        moves += 2

given = 277678

print(f"AoC 2017 Day 3, Part 1 answer is {part1(given)}")
print(f"AoC 2017 Day 3, Part 2 answer is {part2(given)}")

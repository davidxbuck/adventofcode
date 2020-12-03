# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/3
#
from functools import reduce

import numpy as np


class Grid:
    def __init__(self, filename='03'):
        self.grid = np.array(
            [list(row.strip()) for row in open(f'../inputs2020/Advent2020_{filename}.txt', 'r')]).transpose()

    def traverse(self, x, y):
        x_inc = x
        y_inc = y
        max_x, max_y = self.grid.shape
        tree_count = 0

        while y < max_y:
            if self.grid[x, y] == '#':
                tree_count += 1
            x = (x + x_inc) % max_x
            y += y_inc
        return tree_count


grid = Grid(filename="03")
print(f"""AoC 2020 Day 3 Part 1 answer is: {grid.traverse(3, 1)}""")

parameters = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
trees = [grid.traverse(*param) for param in parameters]
print(f"""AoC 2020 Day 3 Part 2 answer is: {reduce(lambda a, b: a * b, trees)}""")

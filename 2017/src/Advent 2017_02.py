# Advent of Code 2017
#
# From https://adventofcode.com/2017/day/2
#
from itertools import combinations

import numpy as np

inputs = np.array([row.strip('\n').split('\t') for row in open(f'../inputs2017/Advent2017_02.txt', 'r')], dtype=int)
print()
print(f"AoC 2017 Day 2, Part 1 answer is {np.sum(np.max(inputs, axis=1) - np.min(inputs, axis=1))}")
comb = [list(combinations(row, 2)) for row in inputs]
print(f"AoC 2017 Day 2, Part 2 answer is {sum([max([x, y]) // min([x, y]) for row in comb for x, y in row if max([x, y]) % min([x, y]) == 0])}")

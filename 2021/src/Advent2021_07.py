# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/7
#
import numpy as np

positions = np.array(list(map(int, [row.strip().split(',') for row in open('../inputs/Advent2021_07.txt', 'r')][0])))

print(f'Day 7, Part 1 {int(np.sum(np.abs(positions - np.median(positions))))}')

fuel = lambda x: x and x + fuel(x - 1) or 0
print(f'Day 7, Part 2 {sum(fuel(abs(int(np.mean(positions)) - pos)) for pos in positions)}')

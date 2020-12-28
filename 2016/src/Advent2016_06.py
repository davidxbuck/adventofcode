# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/6
import numpy as np

msgs = np.array([list(row.strip()) for row in open('../inputs/Advent2016_06.txt', 'r')], dtype=str)

part1 = part2 = ''
for y in range(msgs.shape[1]):
    unique, counts = np.unique(msgs[:, y], return_counts=True)
    part1 += unique[np.argmax(counts)]
    part2 += unique[np.argmin(counts)]

print(f"AoC 2016 Day 6, Part 1 answer is {part1}")
print(f"AoC 2016 Day 6, Part 2 answer is {part2}")
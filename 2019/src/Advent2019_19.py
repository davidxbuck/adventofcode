# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/19
#
from itertools import product

from Advent2019_Intcode import Intcode

inputs = list(map(int, [code.strip().split(',') for code in open('../inputs/Advent2019_19.txt', 'r')][0]))
print(f"AoC 2019 Day 19, Part 1: {sum(Intcode(inputs[:], inp=[x, y], mode='run').run()[0] for x, y in product(range(50), range(50)))}")

x = 100
y = 0
while not Intcode(inputs[:], inp=[x - 99, y + 100], mode='run').run()[0]:
    while not Intcode(inputs[:], inp=[x, y], mode='run').run()[0]:
        y += 1
    x += 1
print(f'AoC 2019 Day 19, Part 2: {(x - 100) * 10000 + y}')
# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/12

import re

data = [re.findall(r'(-?\d+)', row.strip()) for row in open('../inputs/Advent2015_12.json', 'r')]

print(f"AoC 2015 Day 12, Part 1 answer is {sum(int(x[0]) for x in data if x)}")

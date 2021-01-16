# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/8

import re

inp = [row.strip() for row in open('../inputs/Advent2015_08.txt', 'r')]

x1 = re.compile(r'(\\\"|\\\\)')  # things that reduce to a length of 1
x0 = re.compile(r'(\\x.|\")')  # things that reduce to a length of 0
print(f"AoC 2015 Day 8, Part 1 answer is {sum(len(row) - len(x0.sub('', x1.sub('q', row))) for row in inp)}")

part2 = 0
x5 = re.compile(r'(\\x[0-9a-f]{2})')
x4 = re.compile(r'(\\\"|\\\\)')
x2 = re.compile(r'(\")')
print(f"""AoC 2015 Day 8, Part 2 answer is {sum(len(x2.sub('ss', x4.sub('rrrr', x5.sub('qqqqq', row))))
                                                + 2 - len(row) for row in inp)}""")

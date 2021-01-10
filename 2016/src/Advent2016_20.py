# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/20
import re

debug = False
data = sorted([list(map(int, re.findall(r'\d+', row.strip()))) for row in open('../inputs/Advent2016_20.txt', 'r')])

mini, maxi = data[0]
part1 = False
blocked = 0
for x in data[1:]:
    if x[0] > maxi:
        if not part1:
            print(f"AoC 2016 Day 20, Part 1 answer is {maxi + 1}")
            part1 = True
        blocked += maxi - mini + 1
        mini, maxi = x
    if x[1] > maxi:
        maxi = x[1]
blocked += maxi - mini + 1
print(f"AoC 2016 Day 20, Part 2 answer is {4294967296 - blocked}")

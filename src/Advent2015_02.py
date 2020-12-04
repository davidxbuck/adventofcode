# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/2
#
from math import prod
inputs = [data.strip() for data in open('../inputs2015/Advent2015_02.txt', 'r')]
presents = [list(map(int, row.split('x'))) for row in inputs]

ribbon = paper = 0

for l, w, h in presents:
    sides = [l*w, w*h, h*l]
    paper += sum(sides) * 2 + min(sides)
    ribbon += sum(sorted(lengths := [l, w, h])[:2]) * 2 + prod(lengths)

print(f"AoC 2015 Day 2, Part 1 answer is {paper}")
print(f"AoC 2015 Day 2, Part 2 answer is {ribbon}")

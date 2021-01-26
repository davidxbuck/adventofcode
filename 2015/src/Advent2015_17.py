# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/17

from itertools import combinations

inp = [int(row.strip()) for row in open('../inputs/Advent2015_17.txt', 'r')]
print(f"AoC 2015 Day 15, Part 1 answer is: ", end="")
print(sum(sum(sum(x) == 150 for x in combinations(inp, r)) for r in range(1, len(inp))))

for r in range(1, len(inp)):
    if sum(sum(x) == 150 for x in combinations(inp, r)) > 0:
        print(f"AoC 2015 Day 15, Part 2 answer is: ", end="")
        print(sum(sum(x) == 150 for x in combinations(inp, r)))
        break

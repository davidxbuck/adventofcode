# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/3
#

inputs = [data.strip() for data in open('../inputs/Advent2015_03.txt', 'r')][0]

move = {'^': 0 + 1j, ">": 1, "v": 0 - 1j, "<": -1}


def visit(inputs):
    position = 0 + 0j
    visited = {position}
    for x in inputs:
        position = position + move[x]
        visited.add(position)
    return visited


print(f"AoC 2015 Day 3, Part 1 answer is {len(visit(inputs))}")
print(f"AoC 2015 Day 3, Part 2 answer is {len(visit(inputs[0::2]) | visit(inputs[1::2]))}")


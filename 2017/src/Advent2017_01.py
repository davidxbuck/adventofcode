# Advent of Code 2017
#
# From https://adventofcode.com/2017/day/1
#

inp = [data.strip() for data in open('../inputs/Advent2017_01.txt', 'r')][0]

print(f"AoC 2017 Day 1, Part 1 answer is {sum([int(inp[i]) if inp[i] == inp[(i + 1) % len(inp)] else 0 for i in range(0, len(inp))])}")
print(f"AoC 2017 Day 1, Part 2 answer is {sum([int(inp[i]) if inp[i] == inp[(i + (len(inp) // 2)) % len(inp)] else 0 for i in range(0, len(inp))])}")

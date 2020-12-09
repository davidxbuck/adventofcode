# Advent of Code 2017
#
# From https://adventofcode.com/2017/day/4
#

passwords = [row.strip().split() for row in open('../inputs/Advent2017_04.txt', 'r')]
print(sum(len(row) == len(set(row)) for row in passwords))
print(sum(len(row) == len(set("".join(sorted(x)) for x in row)) for row in passwords))

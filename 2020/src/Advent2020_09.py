# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/9
#
entries = list(map(int, [row.strip() for row in open('../inputs/Advent2020_09.txt', 'r')]))

from itertools import combinations

preamble = 25

for pos, part1 in enumerate(entries[preamble:], preamble):
    if part1 not in map(sum, combinations(entries[pos - preamble: pos], 2)):
        print(f'AoC 2020 Day 9, Part 1 answer is {part1}')
        break

found = False
for length in range(2, entries.index(part1) - 1):
    for pos in range(length, entries.index(part1) - 1):
        if sum(entries[pos - length: pos]) == part1:
            print(
                f'AoC 2020 Day 9, Part 2 answer is {min(entries[pos - length: pos]) + max(entries[pos - length: pos])}')
            found = True
            break
    if found:
        break

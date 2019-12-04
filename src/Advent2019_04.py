# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/4
#
import re

START = 136760
STOP = 595730

part1 = part2 = 0

for i in range(START, STOP + 1):
    test = str(i)
    repeats = re.findall(r'(.)\1+', test)
    if repeats and test == "".join(sorted(test)):
        part1 += 1
        for repeat in repeats:
            if test.count(repeat) == 2:
                part2 += 1
                break

print(f'AoC 2019 Day 4, Part 1: {part1}')
print(f'AoC 2019 Day 4, Part 2: {part2}')

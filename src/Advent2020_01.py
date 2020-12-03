# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/1
#
entries = sorted(list(map(int, [row.strip() for row in open('../inputs2020/Advent2020_01.txt', 'r')])))
entry_set = set(entries)

# Manual looping

for x in entries:
    if 2020 - x in entry_set:
        print(f'AoC 2020 Day 1, Part 1 answer is {x}*{2020 - x} = {x * (2020 - x)}')
        break

found = False
for ix, x in enumerate(entries):
    if found:
        break
    for y in range(len(entries) - 1, ix, -1):
        if 2020 - x - entries[y] in entry_set:
            print(f"""AoC 2020 Day 1, Part 2 answer is {
            x}*{entries[y]}*{2020 - x - entries[y]} = {x * entries[y] * (2020 - x - entries[y])}""")
            found = True
            break

# Itertools

from itertools import combinations
from math import prod

for x in combinations(entries, 2):
    if sum(x) == 2020:
        print(f'AoC 2020 Day 1, Part 1 answer is {x} = {prod(x)}')
        break

for x in combinations(entries, 3):
    if sum(x) == 2020:
        print(f'AoC 2020 Day 1, Part 2 answer is {x} = {prod(x)}')
        break

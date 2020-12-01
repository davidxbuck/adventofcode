# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/1
#
entries = list(map(int, [row.strip() for row in open('../inputs2020/Advent2020_01.txt', 'r')]))
entries.sort()
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

from itertools import permutations

for x in permutations(entries, 2):
    if sum(x) == 2020:
        print(f'AoC 2020 Day 1, Part 1 answer is {x} = {x[0] * x[1]}')
        break

for x in permutations(entries, 3):
    if sum(x) == 2020:
        print(f'AoC 2020 Day 1, Part 2 answer is {x} = {x[0] * x[1] * x[2]}')
        break


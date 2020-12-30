# Advent of Code 2017
#
# From https://adventofcode.com/2017/day/08
import re
from collections import defaultdict

data = [re.findall(r'^(\w+) (inc|dec) (-?\d+) if (\w+) (\W+) (-?\d+)$', row.strip())[0] for row in
        open('../inputs/Advent2017_08.txt', 'r')]

registers = defaultdict(int)
maxreg = -99999999999999

for reg, inc, val, compreg, comp, compval in data:
    val = int(val)
    compval = int(compval)

    if inc == 'dec':
        val = - val

    if reg not in registers:
        registers[reg] = 0
    if compreg not in registers:
        registers[compreg] = 0

    if comp == '==': compare = registers[compreg] == compval
    if comp == '<=': compare = registers[compreg] <= compval
    if comp == '>=': compare = registers[compreg] >= compval
    if comp == '!=': compare = registers[compreg] != compval
    if comp == '<':  compare = registers[compreg] < compval
    if comp == '>':  compare = registers[compreg] > compval

    if compare:
        registers[reg] += val
        maxreg = max([registers[reg], maxreg])

print(f'AoC 2017 Day 8, Part 1 answer is {max(registers.values())}')
print(f'AoC 2017 Day 8, Part 2 answer is {maxreg}')

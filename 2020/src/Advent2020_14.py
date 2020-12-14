# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/14
#
import re
from collections import defaultdict


def set_bit(value, bit, index):
    mask = 1 << index
    value &= ~mask
    if bit:
        value |= mask
    return value


def parse_mask(value, mask):
    for ix, bit in enumerate(mask):
        index = 35 - ix
        if bit == "1":
            value = set_bit(value, 1, index)
    return value


def preset(value, mask):
    for ix, bit in enumerate(mask):
        index = 35 - ix
        if bit == "1":
            value = set_bit(value, 1, index)
    return value


def parse_mask2(value, mask):
    x_locs = [ix for ix, val in enumerate(mask) if val == 'X']
    values = []
    for x in range(2 ** len(x_locs)):
        repl = f"{x:0{len(x_locs)}b}"
        for ind, loc in enumerate(x_locs):
            value = set_bit(value, int(repl[ind]), 35 - loc)
        values.append(value)
    return values


filename = ''
inps = [row.strip() for row in open(f'../inputs/Advent2020_14{filename}.txt', 'r')]
memory = defaultdict(str)

for inp in inps:
    if "mask" in inp:
        mask = inp[7:43]
    else:
        loc, val = map(int, re.findall(r"mem\[(\d+)] = (\d+)$", inp)[0])
        memory[loc] = parse_mask(val, mask)

print(f"""AoC 2020 Day 14 Part 1 answer is: {sum(memory.values())}""")

memory = defaultdict(str)

for inp in inps:
    if "mask" in inp:
        mask = inp[7:43]
    else:
        loc, val = map(int, re.findall(r"mem\[(\d+)] = (\d+)$", inp)[0])
        loc = preset(loc, mask)
        for location in parse_mask2(loc, mask):
            memory[location] = val

print(f"""AoC 2020 Day 14 Part 2 answer is: {sum(memory.values())}""")

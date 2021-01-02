# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/15
import re


def solve(filename=''):
    discs = [list(map(int, re.findall(r'^Disc #(\d) has (\d+) positions; at time=(\d), it is at position (\d+).$',
                                      row.strip())[0]))
             for row in open(f'../inputs/Advent2016_15{filename}.txt', 'r')]
    periods = [[period - (period - start + time - disc) % period, period] for disc, period, time, start in discs]
    offset = 0
    period = 1
    for disc_offset, disc_period in periods:
        next_offset = 0
        for x in range(offset, 1000000000000000000000, period):
            if (x + disc_offset) % disc_period == 0:
                if next_offset == 0:
                    next_offset = x
                else:
                    offset = next_offset
                    period = x - next_offset
                    break
    return offset


print(f"AoC 2016 Day 15 Part 1 answer is: {solve()}")
print(f"AoC 2016 Day 15 Part 2 answer is: {solve('b')}")

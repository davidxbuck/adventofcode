# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/10


from itertools import groupby


def expand(count, inp='3113322113'):
    for i in range(count):
        inp = "".join(str(len(grp)) + grp[0] for grp in (''.join(group) for key, group in groupby(inp)))
    return len(inp)


print(f"AoC 2015 Day 10, Part 1 answer is {expand(40)}")
print(f"AoC 2015 Day 10, Part 2 answer is {expand(50)}")

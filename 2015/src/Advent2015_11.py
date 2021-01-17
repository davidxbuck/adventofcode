# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/11

from more_itertools import windowed


def next_password(inp):
    inps = [ord(x) - 97 for x in inp]
    while True:
        inps[-1] += 1
        for x in range(len(inps) - 1, -1, -1):
            if inps[x] > 25:
                inps[x] = 0
                if x > 0:
                    inps[x - 1] += 1
            if inps[x] in [8, 14, 11]:
                inps[x] += 1
                if x < len(inps) - 1:
                    for y in range(x + 1, len(inps)):
                        inps[y] = 0

        seq = False
        for x, y, z in windowed(inps, 3):
            if x + 2 == y + 1 == z:
                seq = True
                break

        pairs = False
        pair = -1
        for x in range(len(inp) - 1):
            if inps[x] == inps[x + 1] and not (x > 0 and inps[x - 1] == inps[x]) and not (
                    x < len(inp) - 2 and inps[x + 2] == inps[x]):
                if pair == -1:
                    pair = inps[x]
                elif pair != inps[x]:
                    pairs = True
                    break

        if pairs and seq:
            return "".join(chr(x + 97) for x in inps)


inp = 'cqjxjnds'
part1 = next_password(inp)
print(f"AoC 2015 Day 11, Part 1 answer is {part1}")
part2 = next_password(part1)
print(f"AoC 2015 Day 11, Part 2 answer is {part2}")

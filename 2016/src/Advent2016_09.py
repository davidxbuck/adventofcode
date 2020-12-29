# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/9
import re

data = [row.strip() for row in open('../inputs/Advent2016_09.txt', 'r')][0]
# data = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
data = re.findall(r'(\(\d+x\d+\)|\w)', data)


def decompress(data):
    decomp = ''
    seq = 0
    while seq < len(data):
        current = data[seq]
        if len(current) == 1:
            decomp += current
        else:
            count, repeat = list(map(int, re.findall(r'(\d+)', current)))
            repeated = ''
            while len(repeated) < count:
                seq += 1
                repeated += data[seq]
            decomp += repeated * repeat
        seq += 1
    return decomp


def decomp_length(data):
    decomp = []
    seq = 0
    while seq < len(data):
        current = data[seq]
        if len(current) == 1:
            decomp.append([1, 1])
        else:
            count, repeat = list(map(int, re.findall(r'(\d+)', current)))
            repeated = []
            len_repeated = 0
            while len_repeated < count:
                seq += 1
                len_repeated += len(data[seq])
                repeated.append(data[seq])
            decomp.append([repeat, decomp_length(repeated)])
        seq += 1
    return decomp


def calc(len_list):
    total = 0
    for repeat, val in len_list:
        if isinstance(val, list):
            val = calc(val)
        total += repeat * val
    return total


print(f"AoC 2016 Day 9, Part 1 answer is {len(decompress(data))}")
print(f"AoC 2016 Day 9, Part 2 answer is {calc(decomp_length(data))}")

# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/4
#
data = [x.split(',') for x in open(f'../inputs/day4.txt', 'r').read().split('\n')]
data = [[list(map(int, x.split('-'))), list(map(int, y.split('-')))] for x, y in data]

contained = []
overlaps = []
for x, y in data:
    a = set(range(x[0], x[1] + 1))
    b = set(range(y[0], y[1] + 1))
    contained.append(True if a | b == a or a | b == b else False)
    overlaps.append(False if len(a) + len(b) == len(a | b) else True)
print(f'Day 4, Part 1 {sum(contained)}')
print(f'Day 4, Part 2 {sum(overlaps)}')

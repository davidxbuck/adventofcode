# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/6
#
from collections import Counter


def lanternfish(days):
    day_counts = initial_counts.copy()
    for _ in range(days):
        day_counts = {k - 1: v for k, v in day_counts.items()}
        if -1 in day_counts:
            day_counts[6] = day_counts[-1] + day_counts.get(6, 0)
            day_counts[8] = day_counts[-1]
            del day_counts[-1]
    return sum(day_counts.values())


initial_counts = Counter(list(map(int, [row.strip().split(',') for row in open('../inputs/Advent2021_06.txt', 'r')][0])))

print(f'Day 6, Part 1 {lanternfish(80)}')
print(f'Day 6, Part 2 {lanternfish(256)}')

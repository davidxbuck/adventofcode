# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/15
#
from collections import defaultdict

numbers = list(map(int, [row.strip().split(',') for row in open('../inputs/Advent2020_15.txt', 'r')][0]))


def day15(numbers, period):
    prev = defaultdict(int, {number: pos for pos, number in enumerate(numbers[:-1], 0)})
    next_number = numbers[-1]
    for x in range(len(numbers) - 1, period - 1):
        if next_number in prev:
            number = x - prev[next_number]
        else:
            number = 0
        prev[next_number] = x
        next_number = number
    return number


print(f'AoC 2020 Day 15, Part 1 answer is {day15(numbers, 2020)}')
print(f'AoC 2020 Day 15, Part 2 answer is {day15(numbers, 30000000)}')

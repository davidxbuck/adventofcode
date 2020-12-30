# Advent of Code 2017
#
# From https://adventofcode.com/2017/day/11

data = [row.strip().split(',') for row in open('../inputs/Advent2017_11.txt', 'r')][0]

moves = {'n': 2j,
         's': -2j,
         'ne': 1 + 1j,
         'nw': -1 + 1j,
         'sw': -1 - 1j,
         'se': 1 - 1j
         }

location = furthest = furthest_steps = 0

for move in data:
    location += moves[move]
    dist = int(location.real + (abs(location.imag) - abs(location.real)) / 2)
    if dist > furthest_steps:
        furthest = location
        furthest_steps = dist

print(f'AoC 2017 Day 8, Part 1 answer is {int(location.real + (abs(location.imag) - abs(location.real)) / 2)}')
print(f'AoC 2017 Day 8, Part 2 answer is {int(furthest.real + (abs(furthest.imag) - abs(furthest.real)) / 2)}')

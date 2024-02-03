# Advent of Code 2023
#
# From https://adventofcode.com/2023/day/2
#

from math import prod

data = [x.split(':') for x in open('../inputs/day2.txt', 'r').read().split('\n')]
data = {x[0].split(' ')[1]: x[1].split(';') for x in data}
test = {'red': 12, 'green': 13, 'blue': 14}
output = {}
for k, v in data.items():
    output[k := int(k)] = []
    for ix, x in enumerate(v):
        moves = x.split(', ')
        output[k].append({})
        for y in moves:
            number, colour = y.strip().split(' ')
            output[k][-1][colour] = int(number)

count = 0
for k, game in output.items():
    valid = True
    for turn in game:
        for colour in test.keys():
            if turn.get(colour, 0) > test[colour]:
                valid = False
    if valid:
        count += k

print(f'Day 2, Part 1 {count}')

power = 0
for k, game in output.items():
    colours = {}
    for turn in game:
        for colour, count in test.items():
            colours[colour] = max((colours.get(colour, 0), turn.get(colour, 0)))
    power += prod(colours.values())

print(f'Day 2, Part 2 {power}')

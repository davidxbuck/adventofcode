# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/6
#
data = open(f'../inputs/day6.txt', 'r').read()

for x in range(len(data)-3):
    if len(set(data[x: x+4])) == 4:
        break

print(f'Day 6, Part 1 {x + 4}')

for x in range(len(data)-3):
    if len(set(data[x: x+14])) == 14:
        break

print(f'Day 6, Part 2 {x + 14}')

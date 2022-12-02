# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/1
#
data = [sum(map(int, x.split('\n'))) for x in open(f'../inputs/day1.txt', 'r').read().split('\n\n')]

print(f'Day 1, Part 1 {max(data)}')
print(f'Day 1, Part 2 {sum(sorted(data)[-3:])}')

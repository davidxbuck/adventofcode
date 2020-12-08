# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/8
#
import copy
from Advent2020_machine import Machine

inputs = [mass.strip().split(' ') for mass in open('../inputs2020/Advent2020_08.txt', 'r')]
inputs = [[x, int(y), False] for x, y in inputs]

_, part1 = Machine(copy.deepcopy(inputs), mode=1, debug=False).run()
print(f'AoC 2020 Day 8, Part 1 answer is {part1}')

pos = 0
while pos < len(inputs):
    new = copy.deepcopy(inputs)
    if new[pos][0] == 'jmp':
        new[pos][0] = 'nop'
        loop, part2 = Machine(copy.deepcopy(new), mode=1, debug=False).run()
    elif new[pos][0] == 'nop':
        new[pos][0] = 'jmp'
        loop, part2 = Machine(copy.deepcopy(new), mode=1, debug=False).run()
    if new[pos][0] in ['jmp', 'nop'] and loop is False:
        print(f'AoC 2020 Day 8, Part 2 answer is {part2}')
        break
    pos += 1


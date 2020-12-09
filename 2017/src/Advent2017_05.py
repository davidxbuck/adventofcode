# Advent of Code 2017
#
# From https://adventofcode.com/2017/day/5
#
from collections import defaultdict

entries = list(map(int, [row.strip() for row in open('../inputs/Advent2017_05.txt', 'r')]))

program = defaultdict(list, enumerate(entries))
pointer = 0
steps = 0
while program.get(pointer) is not None:
    step = program[pointer]
    program[pointer] += 1
    pointer += step
    steps += 1

print(steps)

program = defaultdict(list, enumerate(entries))
pointer = 0
steps = 0
step = 0
while program.get(pointer) is not None:
    step = program[pointer]
    if step >= 3:
        program[pointer] -= 1
    else:
        program[pointer] += 1
    pointer += step
    steps += 1

print(steps)
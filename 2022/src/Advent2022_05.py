# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/5
#
import re
import pandas as pd

stacks, moves = open(f'../inputs/day5.txt', 'r').read().split('\n\n')
moves = [list(map(int, (re.findall(r'move (\d+) from (\d+) to (\d+)', x)[0]))) for x in moves.split('\n')]
stacks = [[x[y] for y in range(1, len(x), 4)] for x in stacks.split('\n')]
stack_names = list(map(int, stacks.pop(-1)))
stacks_df = pd.DataFrame(stacks).fillna(' ')
stacks_df.columns = stack_names

stacks = {stack: [box for box in stacks_df[stack][::-1] if box and box != ' '] for stack in stack_names}
stacks2 = stacks.copy()

for qty, from_, to_ in moves:
    stacks[to_] += stacks[from_][:-qty - 1:-1]
    stacks[from_] = stacks[from_][:-qty]

print(f'Day 5, Part 1 {"".join([stacks[x][-1] for x in stack_names])}')

for qty, from_, to_ in moves:
    stacks2[to_] += stacks2[from_][-qty:]
    stacks2[from_] = stacks2[from_][:-qty]

print(f'Day 5, Part 2 {"".join([stacks2[x][-1] for x in stack_names])}')

# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/18
#
from math import prod

filename = ''

# Inputs
sums = [row.strip().replace('(', '( ').replace(')', ' )').split(' ') for row in
        open(f'../inputs/Advent2020_18{filename}.txt', 'r')]
sums = [[int(x) if x.isdigit() else x for x in part] for part in sums]


def compute(part, step=1):
    if step == 1:
        result = int(part[0])
        for x in part[1:]:
            if x in ['*', '+']:
                sign = x
                continue
            if sign == '+':
                result += x
            else:
                result *= x
    elif step == 2:
        while '+' in part:
            ix = part.index('+')
            part = part[:ix - 1] + [part[ix - 1] + part[ix + 1]] + part[ix + 2:]
        result = prod(part[0::2])
    return result


def resolve(part, step=1):
    while part.count('(') > 0:
        for ix, x in enumerate(part):
            if x == '(':
                pos = ix
            elif x == ')':
                part = part[:pos] + [compute(part[pos + 1:ix], step)] + part[ix + 1:]
                break # Rather inefficient to restart the loop after resolving one bracket
    return compute(part, step)


print(f"""AoC 2020 Day 18 Part 1 answer is: {sum(resolve(x) for x in sums)}""")
print(f"""AoC 2020 Day 18 Part 2 answer is: {sum(resolve(x, 2) for x in sums)}""")


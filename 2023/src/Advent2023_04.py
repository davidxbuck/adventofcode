# Advent of Code 2023
#
# From https://adventofcode.com/2023/day/4
#


import numpy as np

data = np.array([x.split(':') for x in open('../inputs/day4.txt', 'r').read().split('\n')])
split_data = {}
for key, numbers in data:
    key = int(key.split(' ')[-1])
    winning, my_numbers = numbers.replace('  ', ' ').split('|')
    winning = set(winning.strip().split(' '))
    my_numbers = set(my_numbers.strip().split(' '))
    split_data[key] = (
    winning, my_numbers, (l := winning.intersection(my_numbers)), len(l), 2 ** (len(l) - 1) if l else 0)
print(f'Day 4, Part 1 {sum(x[4] for x in split_data.values())}')

tickets = {x: 1 for x in split_data.keys()}
for k, v in split_data.items():
    won_tix = v[3]
    qty = tickets[k]
    for keys in range(k + 1, k + 1 + won_tix):
        tickets[keys] += qty
print(f'Day 4, Part 2 {sum(tickets.values())}')

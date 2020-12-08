# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/2
#
import numpy as np

MOVES = {'L': [0, -1],
         'R': [0, 1],
         'U': [-1, 0],
         'D': [1, 0],
         }

pad1 = np.array([['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']])
pad2 = np.array([[None, None, '1', None, None],
                 [None, '2', '3', '4', None],
                 ['5', '6', '7', '8', '9'],
                 [None, 'A', 'B', 'C', None],
                 [None, None, 'D', None, None]])


def get_pin(pad, start_key='5', filename=''):
    pin = ''
    keys = (row.strip() for row in open(f'../inputs2016/Advent2016_02{filename}.txt', 'r'))

    a, b = pad.shape
    keymap = np.full((a + 2, b + 2), None)
    keymap[1:1 + a, 1:1 + b] = pad
    position = np.array([np.where(keymap == start_key)[0][0], np.where(keymap == start_key)[1][0]])

    for moves in keys:
        for move in moves:
            if keymap[tuple(position + MOVES[move])]:
                position += MOVES[move]

        pin += keymap[tuple(position)]
    return pin


print(f"""AoC 2016 Day 2 Part 1 answer is: {get_pin(pad1)}""")
print(f"""AoC 2016 Day 2 Part 2 answer is: {get_pin(pad2)}""")

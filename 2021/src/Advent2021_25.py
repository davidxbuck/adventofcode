# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/25
#
import numpy as np

grid = np.array([list(row.rstrip()) for row in open('../inputs/Advent2021_25.txt', 'r')], dtype=str)
max_x, max_y = grid.shape
counter = 0


def print_grid(grid):
    print('-' + "-\n-".join(["".join(x) for x in grid.astype(str).tolist()]).replace('0', '.').replace('1', '#') + '-')


while True:
    counter += 1

    pos_right = list(np.where(grid == '>'))
    post = (pos_right[1].copy() + 1) % max_y
    right_check = grid[pos_right[0], post] == '.'
    pos_right = [x[right_check] for x in pos_right]
    post = post[right_check]
    grid[tuple(pos_right)] = '.'
    grid[pos_right[0], post] = '>'

    pos_down = list(np.where(grid == 'v'))
    post = (pos_down[0].copy() + 1) % max_x
    down_check = grid[post, pos_down[1]] == '.'
    pos_down = [x[down_check] for x in pos_down]
    post = post[down_check]
    grid[tuple(pos_down)] = '.'
    grid[post, pos_down[1]] = 'v'
    if len(pos_right[0]) + len(pos_down[0]) == 0:
        break
print(f'Day 25, Part 1: {counter}')

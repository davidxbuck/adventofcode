# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/8
#
import numpy as np

trees = np.array([list(map(int, list(x))) for x in open(f'../inputs/day8.txt', 'r').read().split('\n')], dtype=int)

visible = np.full(trees.shape, False, dtype=bool)
for x in range(trees.shape[0]):
    for y in range(trees.shape[1]):
        if x in (0, trees.shape[0] - 1) or y in (0, trees.shape[1] - 1) or min(
                [np.max(trees[0:x, y]), np.max(trees[x, 0:y]), np.max(trees[x + 1:, y]), np.max(trees[x, y + 1:])]) < \
                trees[x, y]:
            visible[x, y] = True

print(f'Day 8, Part 1 {np.sum(visible)}')

score = np.full(trees.shape, 0, dtype=int)
for x in range(1, trees.shape[0] - 1):
    for y in range(1, trees.shape[1] - 1):
        up = trees[x - 1::-1, y]
        down = trees[x + 1:, y]
        right = trees[x, y + 1:]
        left = trees[x, y - 1::-1]
        val = 1
        for direction in [up, down, left, right]:
            sight_line = direction >= trees[x, y]
            tree_index = np.where(sight_line == True)[0]
            tree_count = tree_index[0] + 1 if len(tree_index) > 0 else len(direction)
            val *= tree_count
        score[x, y] = val

print(f'Day 8, Part 2 {np.max(score)}')

# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/13
#
import numpy as np
import networkx as nx
from queue import Queue
import matplotlib.pyplot as plt

inp = [row.strip().split(',') for row in open("../inputs/Advent2021_13.txt", "r")]
dots = np.array([[int(x) for x in row] for row in inp if len(row) == 2])
folds = [row[0].split()[2].split('=') for row in inp[len(dots) + 1:]]

sheet = np.zeros(tuple(np.max(dots, axis=0) + 1), dtype=bool)
for x, y in dots:
    sheet[x, y] = True
sheet = sheet.T

for ix, fold in enumerate(folds):
    axis, row = fold
    row = int(row)
    if axis == 'y':
        left = sheet[:row, :]
        right = sheet[row+1:, :]
        right_flipped = np.flipud(right)
        if right_flipped.shape[0] < left.shape[0]:
            diff = left.shape[0] - right_flipped.shape[0]
            new_right_flipped = np.zeros(left.shape, dtype=bool)
            new_right_flipped[diff:, :] = right_flipped
            right_flipped = new_right_flipped
        elif right_flipped.shape[0] > left.shape[0]:
            diff = right_flipped.shape[0] - left.shape[0]
            new_left = np.zeros(right_flipped.shape, dtype=bool)
            new_left[diff:, :] = left
            left = new_left
        sheet = left + right_flipped
    elif axis == 'x':
        top = sheet[:, :row]
        bottom = sheet[:, row + 1:]
        bottom_flipped = np.fliplr(bottom)
        if bottom_flipped.shape[1] < top.shape[1]:
            diff = top.shape[1] - bottom_flipped.shape[1]
            new_bottom_flipped = np.zeros(top.shape, dtype=bool)
            new_bottom_flipped[:, diff:] = bottom_flipped
            bottom_flipped = new_bottom_flipped
        elif bottom_flipped.shape[1] > top.shape[1]:
            diff = bottom_flipped.shape[1] - top.shape[1]
            new_top = np.zeros(bottom_flipped.shape, dtype=bool)
            new_top[:, diff:] = top
            top = new_top
        sheet = top + bottom_flipped
    if ix == 0:
        print(f'Day 13, Part 2 {np.sum(sheet)}')

# Visualisation

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(13, 2)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(sheet, aspect='equal')
plt.savefig('Advent2021_13.png', dpi=300)
plt.show()

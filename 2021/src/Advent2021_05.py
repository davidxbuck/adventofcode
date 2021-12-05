# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/5
#
import numpy as np
import re

data = [row.strip() for row in open('../inputs/Advent2021_05.txt', 'r')]
all_fields = [list(map(int, re.findall(r'^(\d+),(\d+) -> (\d+),(\d+)$', entry)[0])) for entry in data]
up_and_down = [x for x in all_fields if x[0] == x[2] or x[1] == x[3]]

grid = np.zeros((max(sum(up_and_down, [])) + 1, max(sum(up_and_down, [])) + 1), dtype=int)

for y1, x1, y2, x2 in up_and_down:
    if x1 < x2 or y1 < y2:
        grid[x1:x2 + 1, y1:y2 + 1] += 1
    else:
        grid[x2:x1 + 1, y2:y1 + 1] += 1
print(f'Day 4, Part 1 {np.sum(grid > 1)}')

diagonal = [x for x in all_fields if x[0] != x[2] and x[1] != x[3]]

for y1, x1, y2, x2 in diagonal:
    flip = not ((x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2))
    tl_x, tl_y = (min(x1, x2), min(y1, y2))
    width = abs(x1 - x2) + 1
    identity = np.identity(width, dtype=int)
    if flip:
        identity = np.fliplr(identity)
    grid[tl_x:tl_x + width, tl_y: tl_y + width] += identity
print(f'Day 4, Part 2 {np.sum(grid > 1)}')

# Visualisation

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(10, 10)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
plt.set_cmap('hot')
ax.imshow(grid, aspect='equal')
plt.savefig('Advent2021_05.png', dpi=300)

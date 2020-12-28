# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/8
import re
import numpy as np
import matplotlib.pyplot as plt

cmds = [re.findall(r'.?(rect|row|column)\D+(\d+)\D+(\d+)$', row.strip())[0] for row in
        open('../inputs/Advent2016_08.txt', 'r')]

screen = np.full((6, 50), False)

for cmd, x, y in cmds:
    x = int(x)
    y = int(y)
    if cmd == 'rect':
        screen[0:y, 0:x] = True
    if cmd == 'column':
        col = screen[:, x]
        col = np.concatenate((col[len(col) - y:], col[:len(col) - y]))
        screen[:, x] = col
    if cmd == 'row':
        row = screen[x, :]
        row = np.concatenate((row[len(row) - y:], row[:len(row) - y]))
        screen[x, :] = row

print(np.sum(np.sum(screen)))

plt.imshow(screen)
plt.show()

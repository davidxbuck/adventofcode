# Advent of Code 2018 Day 13
#
# Read file and extract dependencies

file = open("Advent13.txt", 'r')
input = [row[:-1] for row in file]

from operator import add

import numpy as np


def visualise_grid():
    outgrid = np.copy(grid)
    for a, b, c, d in carts:
        outgrid[b[0], b[1]] = c

    for i in range(gridsize):
        print("".join(outgrid[i]))


gridsize = 150
grid = np.empty([gridsize, gridsize], dtype=str)
carts = []
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# populate grid with track and extract carts

for x in range(gridsize):
    for y in range(len(input[x])):
        if input[x][y] in "^":  # [cartno[0], position[1], direction[2], next turn[3]]
            carts.append([len(carts), [x, y], 0, -1])
            grid[x, y] = "|"
        elif input[x][y] in ">":
            carts.append([len(carts), [x, y], 1, -1])
            grid[x, y] = "-"
        elif input[x][y] in "v":
            carts.append([len(carts), [x, y], 2, -1])
            grid[x, y] = "|"
        elif input[x][y] in "<":
            carts.append([len(carts), [x, y], 3, -1])
            grid[x, y] = "-"

        else:
            grid[x, y] = input[x][y]

numcarts = len(carts)
loop = 0

crash = False

while not crash:
    move_order = [y[0] for y in sorted(carts, key=lambda x: x[1])]
    new_scratch = [None for _ in range(numcarts)]
    new_positions = [None for _ in range(numcarts)]
    for move in move_order:
        new_positions[move] = list(map(add, carts[move][1], dir[carts[move][2]]))
        newgrid = grid[new_positions[move][0], new_positions[move][1]]
        new_scratch[move] = newgrid
        for k in range(numcarts):
            if carts[k][1] == new_positions[move]:
                crash_position = [new_positions[move][1], new_positions[move][0]]
                crash = True
                break
        if crash == True:
            break
        if newgrid == "/":  # ^ becomes >, > becomes ^, < becomes v, v becomes <
            if carts[move][2] == 0:
                carts[move][2] = 1
            elif carts[move][2] == 1:
                carts[move][2] = 0
            elif carts[move][2] == 2:
                carts[move][2] = 3
            elif carts[move][2] == 3:
                carts[move][2] = 2
        if newgrid == "\\":  # ^ becomes <, > becomes v, < becomes ^, v becomes >
            if carts[move][2] == 0:
                carts[move][2] = 3
            elif carts[move][2] == 1:
                carts[move][2] = 2
            elif carts[move][2] == 2:
                carts[move][2] = 1
            elif carts[move][2] == 3:
                carts[move][2] = 0
        if newgrid == "+":
            carts[move][2] = (carts[move][2] + carts[move][3]) % 4  # new direction
            carts[move][3] = (carts[move][3] + 2) % 3 - 1  # next direction
        carts[move][1] = new_positions[move]

visualise_grid()

print("Part 1 - Crash", crash_position, "evaluated after", loop, "iterations")

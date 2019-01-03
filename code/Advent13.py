# Advent of Code 2018 Day 13
#

from operator import add

import numpy as np

# Read file and extract dependencies

file = open("Advent13.txt", 'r')
input = [row[:-1] for row in file]


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
arrows = "^>v<"

# populate grid with track and extract carts

for x in range(gridsize):
    for y in range(len(input[x])):
        if input[x][y] in arrows:  # [cartno[0], position[1], direction[2], next turn[3]]
            carts.append([len(carts), [x, y], arrows.index(input[x][y]), -1])
            grid[x, y] = input[x][y].translate(str.maketrans(arrows, "|-|-"))
        else:
            grid[x, y] = input[x][y]

numcarts = len(carts)
tick = 0

crash = False

while not crash:
    tick += 1
    move_order = [y[0] for y in sorted(carts, key=lambda x: x[1])]

    for move in move_order:
        new_position = list(map(add, carts[move][1], dir[carts[move][2]]))
        newgrid = grid[new_position[0], new_position[1]]
        for k in range(numcarts):
            if carts[k][1] == new_position:
                crash_position = [new_position[1], new_position[0]]
                crash = True
                break
        if crash == True:
            break
        if newgrid == "/":  # ^0 becomes >1, >1 becomes ^0, v2 becomes <3, <3 becomes v2
            carts[move][2] = (5 - carts[move][2]) % 4

        if newgrid == "\\":  # ^0 becomes <3, >1 becomes v2, v2 becomes >1, <3 becomes ^0
            carts[move][2] = (3 - carts[move][2]) % 4

        if newgrid == "+":
            carts[move][2] = (carts[move][2] + carts[move][3]) % 4  # new direction
            carts[move][3] = (carts[move][3] + 2) % 3 - 1  # next direction
        carts[move][1] = new_position

visualise_grid()

print("Part 1 - Crash", crash_position, "evaluated after", tick, "iterations")

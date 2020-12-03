# Advent of Code 2018 Day 17
#
# Sample inputs
# x=268, y=1520..1521
# x=547, y=316..341
# y=417, x=297..313

import itertools
import re

import numpy as np


class Drop(object):
    newid = itertools.count()

    def __init__(self, x, y):
        self.id = next(self.__class__.newid)
        self.x = x
        self.y = y
        self.prevx = -1
        self.prevy = -1
        self.active = True

    def __str__(self):
        if self.active:
            return "Drop {} at ({},{}). Now active.".format(self.id, self.x, self.y)
        else:
            return "Drop {} at ({},{}). Now inactive.".format(self.id, self.x, self.y)

    def move(self):
        self.down()
        self.spread()
        if grid[self.x, self.y - 1] == "~":  # underwater
            self.active = False
            return
        if self.x == self.prevx and self.y == self.prevy:

            print("XX")
            self.active = False
            return
        else:
            self.prevx = self.x
            self.prevy = self.y

    def down(self):
        if grid[self.x, self.y + 1] == "|":
            self.active = False
            return
        while self.y < maxy and grid[self.x, self.y + 1] == ".":
            self.y += 1
            grid[self.x, self.y] = "|"
        if self.y >= maxy - 1:
            self.active = False
            return

    def spread(self):
        if not self.active:
            return
        if grid[self.x, self.y + 1] == ".":
            print("an error has occurred")
            quit()
        leftx = self.x
        rightx = self.x
        print("Left")
        # Left
        while leftx >= minx and grid[leftx - 1, self.y] != "#":

            if grid[leftx, self.y + 1] == "." or grid[leftx, self.y + 1] == "|":
                self.x = leftx
                break  # stop if the drop is now over empty space
            grid[leftx, self.y] = "|"
            leftx -= 1
            grid[leftx, self.y] = "|"
        # Right
        print("right")
        while rightx <= maxx and grid[rightx + 1, self.y] != "#":
            if grid[rightx, self.y + 1] == "|":
                break
            rightx += 1
            grid[rightx, self.y] = "|"
            if grid[rightx, self.y + 1] == ".":
                if any(dd.x == rightx and dd.y == self.y for dd in drops):
                    pass
                else:
                    drops.append(Drop(rightx, self.y))  # instantiate new drop
                break  # stop if the drop is now over empty space
        #
        print("up")
        # If both sides are container, move up a level and start again.
        if grid[leftx - 1, self.y] == "#" and grid[rightx + 1, self.y] == "#":
            grid[leftx:rightx + 1, self.y] = "~"
            self.y -= 1
            self.spread()


def visualise_grid(show_drops):
    print_grid = np.copy(grid)
    for drop in drops:
        if drop.active:
            print_grid[drop.x, drop.y] = "A"
        else:
            print_grid[drop.x, drop.y] = "X"
    max_print = max([drop.y for drop in drops]) + 10
    for ix, row in enumerate(print_grid.transpose().tolist()):
        if ix > max_print: break
        print("${}$".format("".join(row)[minx:maxx]))
    print("$" * (maxx + 2 - minx))
    print()
    if show_drops:
        for drop in drops: print(drop)
        print()


# Read file and extract dependencies

file = open("../inputs2018/Advent17", 'r')
input = [row.strip().split(", ") for row in file]
x = []
y = []
for row in input:
    i, j = row
    ixy, ival = i.split('=')
    match = re.search(r'[x-y]=(\d{1,})\.\.(\d{1,})', j)
    jvalstart = int(match.group(1))
    jvalstop = int(match.group(2)) + 1
    if ixy == "x":
        x.append([int(ival), int(ival) + 1])
        y.append([int(jvalstart), int(jvalstop)])
    else:
        y.append([int(ival), int(ival) + 1])
        x.append([int(jvalstart), int(jvalstop)])

xa = np.array(x).flatten()
ya = np.array(y).flatten()
minx = np.min(xa) - 1
miny = np.min(ya)
maxx = np.max(xa) + 1
maxy = np.max(ya)

grid = np.full(shape=[maxx + 1, maxy + 1], fill_value=".", dtype=str)
grid[500, 0] = "+"
drops = [Drop(500, 0)]
for i, j in zip(x, y):
    grid[i[0]:i[1], j[0]:j[1]] = "#"

loop = 0
while len(list(filter(lambda x: x.active, drops))) > 0:
    print("Loop", loop)
    loop += 1
    for drop in list(filter(lambda x: x.active, drops)):
        drop.move()

visualise_grid(show_drops=False)

extract = grid[minx:maxx, miny:maxy].flatten()
unique, counts = np.unique(extract, return_counts=True)
a = dict(zip(unique, counts))

print("Dimensions of grid - x: [{},{}], y: [{},{}]".format(minx, maxx, miny, maxy))
print("Step1 - Tiles water can reach:", a["|"] + a["~"])
print("Step2 - Tiles with water after spring stops", a["~"])

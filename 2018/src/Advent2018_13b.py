# Advent of Code 2018 Day 13 Part 2
#
import itertools
from operator import add

import numpy as np


class Cart(object):
    newid = itertools.count()

    def __init__(self, x, y, direction, next_turn=-1):
        self.id = next(self.__class__.newid)
        self.x = x
        self.y = y
        self.direction = "^>v<".index(direction)
        self.next_direction = next_turn
        self.crashed = False

    def __str__(self):
        return "Cart {}, position {}, direction {}, next turn is: {}".format(self.id, self.coords,
                                                                             self.direction, self.next_direction)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x * gridsize + self.y < other.x * gridsize + other.y

    @property
    def coords(self):
        return [self.x, self.y]

    def move(self):
        if not self.crashed:
            new_coords = list(map(add, self.coords, dir[self.direction]))
            self.crash_check(new_coords)
            self.x, self.y = new_coords
            if str(grid[self.x, self.y]) in "+/\\":
                self.turn(grid[self.x, self.y])
        return self.crashed

    def crash_check(self, new_pos):
        for cart in carts:
            if new_pos == cart.coords:
                print("Crash between Cart {} and Cart {} at location {} on tick {}".format(cart.id, self.id, new_pos,
                                                                                           tick))
                self.crashed = cart.crashed = True
                cart.x = cart.y = self.x = self.y = None
                return

    def turn(self, way):
        if way == "/":  # ^0 becomes >1, >1 becomes ^0, v2 becomes <3, <3 becomes v2
            self.direction = (5 - self.direction) % 4
        elif way == "\\":  # ^0 becomes <3, >1 becomes v2, v2 becomes >1, <3 becomes ^0
            self.direction = (3 - self.direction) % 4
        elif way == "+":
            self.direction = (self.direction + self.next_direction) % 4
            self.next_direction = (self.next_direction + 2) % 3 - 1  # next direction


def visualise_grid():
    outgrid = np.copy(grid)
    for cart in carts:
        outgrid[cart.x, cart.y] = cart.direction
        print(cart)

    for i in range(gridsize):
        print("".join(outgrid[i]))


if __name__ == "__main__":

    # Read file and extract dependencies

    file = open("../inputs/Advent13", 'r')
    input = [row.replace("\n", "") for row in file]

    gridsize = 150
    grid = np.empty([gridsize, gridsize], dtype=str)
    carts = []
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # populate grid with track and extract carts

    for x in range(gridsize):
        for y in range(len(input[x])):
            if input[x][y] in "^>v<":  # [cartno[0], position[1], direction[2], next turn[3]]
                carts.append(Cart(x, y, input[x][y]))
                grid[x, y] = input[x][y].translate(str.maketrans("^>v<", "|-|-"))
            else:
                grid[x, y] = input[x][y]

    numcarts = len(carts)
    tick = 0

    visualise_grid()
    while len(carts) > 1:
        tick += 1
        crashes = 0
        for cart in sorted(carts):  # process carts in order of their x, y position
            crashed = cart.move()  # move cart, check for crash
            if crashed: crashes += 1

        if crashes > 0:
            for x in range(len(carts) - 1, -1, -1):  # remove crashed carts from list in reverse order
                if carts[x].crashed:
                    popped = carts.pop(x)

    # visualise_grid()

    print("Part 2 - Crash evaluated after {} iterations. Last cart is Cart {} at ({},{})".format(tick, carts[0].id,
                                                                                                 carts[0].y,
                                                                                                 carts[0].x))

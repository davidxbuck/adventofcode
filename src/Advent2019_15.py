# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/15
#
from itertools import product

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from Advent2019_Intcode import Intcode


class Robot(object):
    dX = {1: 0, 2: 0, 3: -1, 4: 1}
    dY = {1: 1, 2: -1, 3: 0, 4: 0}
    back = {1: 2, 2: 1, 3: 4, 4: 3}

    def __init__(self, code):
        self.x = 21
        self.y = 19
        self.code = code
        self.program = Intcode(self.code, inp=[], mode='run')
        self.stack = []
        self.found = []
        self.grid = np.full([41, 41], -1, dtype=int)
        self.grid[self.x, self.y] = 1
        self.explore()

    def step(self, direction):
        self.program.next_inp(direction)
        result = self.program.run()[0]
        if result:
            self.x += Robot.dX[direction]
            self.y += Robot.dY[direction]
        return result

    def explore(self):
        for direction in range(1, 5):
            if self.grid[self.x + Robot.dX[direction], self.y + Robot.dY[direction]] == -1:
                result = self.step(direction)
                if result == 2:
                    self.found = [self.x, self.y]
                if result:
                    self.grid[self.x, self.y] = 1
                    self.step(Robot.back[direction])
                    self.stack.append(["N", direction])
                else:
                    self.grid[self.x + Robot.dX[direction], self.y + Robot.dY[direction]] = 0

    def move(self):
        while self.stack:
            move_type, direction = self.stack.pop()
            self.step(direction)

            if move_type == "N":
                self.stack.append(["R", Robot.back[direction]])
                self.explore()


def main():
    inputs = list(map(int, [code.strip().split(',') for code in open('../inputs2019/Advent2019_15.txt', 'r')][0]))
    robot = Robot(inputs[:])
    robot.move()

    G = nx.Graph()
    for x, y in product(range(41), range(41)):
        if robot.grid[x, y] == 1:
            if robot.grid[x + 1, y] == 1:
                G.add_edge((x, y), (x + 1, y))
            if robot.grid[x, y + 1] == 1:
                G.add_edge((x, y), (x, y + 1))
    print(f"AoC 2019 Day 15, Part 1: {nx.shortest_path_length(G, source=(21, 19), target=tuple(robot.found))}")

    longest_path = 0
    for node in list(G.nodes):
        path = nx.shortest_path_length(G, source=node, target=tuple(robot.found))
        if path > longest_path:
            longest_path = path

    print(f"AoC 2019 Day 15, Part 2: {longest_path}")

    robot.grid[robot.grid == -1] = 0
    robot.grid[21, 19] = 2
    robot.grid[robot.found[0], robot.found[1]] = 3
    plt.imshow(robot.grid)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()

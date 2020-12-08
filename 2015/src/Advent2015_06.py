# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/6
#

import re

import numpy as np


def importer():
    inputs = [data.strip() for data in open('../inputs/Advent2015_06.txt', 'r')]
    return [re.findall(r"^(turn off|turn on|toggle)\D*(\d+),(\d+)\D*(\d+),(\d+)$", entry)[0] for entry in inputs]


def switch(commands, part=1):
    grid = np.zeros((1000, 1000), dtype=int)
    for record in commands:
        command = record[0]
        x1, y1, x2, y2 = map(int, record[1:])
        if part == 1:
            if command == 'turn on':
                grid[x1: x2 + 1, y1: y2 + 1] = 1
            elif command == 'turn off':
                grid[x1: x2 + 1, y1: y2 + 1] = 0
            else:
                grid[x1: x2 + 1, y1: y2 + 1] = 1 - grid[x1: x2 + 1, y1: y2 + 1]
        elif part == 2:
            if command == 'turn on':
                grid[x1: x2 + 1, y1: y2 + 1] += 1
            elif command == 'turn off':
                grid[x1: x2 + 1, y1: y2 + 1] -= 1
                grid[x1: x2 + 1, y1: y2 + 1][grid[x1: x2 + 1, y1: y2 + 1] < 0] = 0
            else:
                grid[x1: x2 + 1, y1: y2 + 1] += 2
    return np.sum(np.sum(grid))


commands = importer()
print(f"AoC 2015 Day 6, Part 1 answer is {switch(commands, 1)}")
print(f"AoC 2015 Day 6, Part 2 answer is {switch(commands, 2)}")

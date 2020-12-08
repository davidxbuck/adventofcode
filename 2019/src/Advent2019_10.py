# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/6
#
from collections import defaultdict
from math import atan2

import numpy as np


class Day10(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            inputs = [list(line.strip()) for line in f]
            self.asteroid_map = np.array(inputs)
            self.boolean_asteroid_map = (self.asteroid_map == '#')
            self.x_size, self.y_size = self.asteroid_map.shape[0:2]

    def create_angle_grid(self):
        self.angle_grid = np.empty((self.x_size * 2, self.y_size * 2))
        for x in range(self.x_size * 2):
            for y in range(self.y_size * 2):
                if not (x == self.x_size and y == self.y_size):
                    self.angle_grid[x, y] = atan2(y - self.y_size, x - self.x_size)

    def part1_solver(self):
        self.create_angle_grid()
        self.visible_asteroids = np.zeros((self.x_size, self.y_size), dtype=int)
        for testx in range(self.x_size):
            for testy in range(self.y_size):
                if self.boolean_asteroid_map[testx, testy]:
                    copy_grid = np.copy(self.boolean_asteroid_map)
                    copy_grid[testx, testy] = False  # Eliminate self
                    matched_angle_grid = self.angle_grid[self.x_size - testx: self.x_size * 2 - testx,
                                         self.y_size - testy: self.y_size * 2 - testy]
                    self.visible_asteroids[testx, testy] = len(np.unique(matched_angle_grid[copy_grid]))
        self.location = np.unravel_index(self.visible_asteroids.argmax(), self.visible_asteroids.shape)
        return self.location, self.visible_asteroids[self.location]

    def create_distance_grid(self):
        startx, starty = self.location
        self.distance_grid = np.zeros((self.x_size, self.y_size))
        for x in range(self.x_size):
            for y in range(self.y_size):
                self.distance_grid[x, y] = abs(x - startx) + abs(y - starty)

    def part2_solver(self):
        self.boolean_asteroid_map[self.location] = False
        self.create_distance_grid()
        startx, starty = self.location
        self.asteroids_by_angle = defaultdict(list)
        angles = self.angle_grid[self.x_size - startx: self.x_size * 2 - startx,
                 self.y_size - starty: self.y_size * 2 - starty]

        for next_asteroid in range(self.x_size):
            for y in range(self.y_size):
                if self.boolean_asteroid_map[next_asteroid, y]:
                    self.asteroids_by_angle[angles[next_asteroid, y]].append(
                        [[next_asteroid, y], self.distance_grid[next_asteroid, y]])

        iterator = sorted(list(np.unique(angles)), reverse=True)
        self.destorder = []
        while iterator:
            next_iterator = []
            for value in iterator:
                if self.asteroids_by_angle[value]:
                    if len(self.asteroids_by_angle[value]) > 1:
                        next_iterator.append(value)
                    self.asteroids_by_angle[value].sort(key=lambda x: x[1], reverse=True)
                    next_asteroid = self.asteroids_by_angle[value].pop()
                    self.destorder.append(next_asteroid[0])
            iterator = next_iterator


def main():
    filename = '../inputs/Advent2019_10.txt'
    # filename = '../tests/test_Advent2019_10c.txt'
    day10 = Day10(filename)
    location, visible = day10.part1_solver()
    print(f'AoC 2019 Day 10, Part 1: {location[::-1]} with {visible} visible asteroids')

    day10.part2_solver()
    print(f'AoC 2019 Day 10, Part 2: {day10.destorder[199][::-1]}')


if __name__ == '__main__':
    main()

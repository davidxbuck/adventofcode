# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/12
#

import re
from itertools import combinations

import numpy as np


class Moon(object):

    def __init__(self, positions, velocities=[0, 0, 0]):
        self.positions = positions[:]
        self.velocities = velocities[:]

    @property
    def potential(self):
        return sum(map(abs, self.positions))

    @property
    def kinetic(self):
        return sum(map(abs, self.velocities))


class System(object):
    def __init__(self):
        self.moons = []

    def add_moon(self, moon):
        self.moons.append(Moon(moon))

    def gravity(self):
        for a, b in combinations(range(len(self.moons)), 2):
            for i in range(3):
                if self.moons[a].positions[i] > self.moons[b].positions[i]:
                    self.moons[a].velocities[i] -= 1
                    self.moons[b].velocities[i] += 1
                elif self.moons[a].positions[i] < self.moons[b].positions[i]:
                    self.moons[a].velocities[i] += 1
                    self.moons[b].velocities[i] -= 1

    def velocity(self):
        for moon in self.moons:
            for i in range(3):
                moon.positions[i] += moon.velocities[i]

    @property
    def potential(self):
        return sum(moon.potential for moon in self.moons)

    @property
    def kinetic(self):
        return sum(moon.kinetic for moon in self.moons)

    @property
    def total(self):
        return sum(moon.kinetic * moon.potential for moon in self.moons)

with open('../inputs2019/Advent2019_12.txt', 'r') as f:

    input_moons = [list(map(int, re.findall(r"^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$", x.strip())[0])) for x in f]

system = System()
for moon in input_moons[:]:
    system.add_moon(moon)

for x in range(1000):
    system.gravity()
    system.velocity()

print(f'AoC 2019 Day 12 Part 1: {system.total}')

system = System()
for moon in input_moons[:]:
    system.add_moon(moon)

periodicity = [0, 0, 0]
next_axis = [0, 1, 2]
axis = next_axis[:]
start_positions = np.array([moon.positions[:] for moon in system.moons]).transpose()
start_velocities = np.array([moon.velocities[:] for moon in system.moons]).transpose()

for x in range(1, 10000000):
    system.gravity()
    system.velocity()
    for axis in axis:
        if all([moon.positions[axis] for moon in system.moons] == start_positions[axis]) and all(
                [moon.velocities[axis] for moon in system.moons] == start_velocities[axis]):
            periodicity[axis] = x
            next_axis.remove(axis)
    axis = next_axis[:]
    if not axis:
        break

print(f'AoC 2019 Day 12 Part 2: {np.lcm.reduce(periodicity)}')
print()

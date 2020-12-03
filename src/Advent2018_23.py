# Advent of Code 2018 Day 23

# Read file and extract nanobots and positions

import re

file = open("../inputs2018/Advent23", 'r')

nanobots = [list(map(int, re.search("pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", row).group(1, 2, 3, 4))) for row in file]
nanobots = sorted(nanobots, key=lambda x: x[3], reverse=True)

target = nanobots[0]
radius = target.pop()

dist = []
for bot in nanobots:
    dist.append(sum([abs(bot[x]-target[x]) for x in range(3)]))

print("Step1 - Nanobots in range of most powerful bot:", sum(1 for x in dist if x <= radius))

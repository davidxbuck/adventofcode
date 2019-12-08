# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/8
#
import matplotlib.pyplot as plt
import numpy as np

with open('../inputs2019/Advent2019_08.txt', 'r') as f:
    pictures = np.array(list(map(int, list(f.readline().strip())))).reshape(-1, 150)
zeroes = 150 - np.count_nonzero(pictures, axis=1)
least_zeroes = np.argmin(zeroes)
selected = pictures[least_zeroes, :]
vals, counts = np.unique(selected, return_counts=True)
print(f'AoC 2019 Day 8, Part 1: {counts[1]*counts[2]}')


target = np.full(150, 2)

for picture in pictures:
    target = np.where(target == 2, picture, target)

target = target.reshape(6,25)
plt.imshow(target)
plt.show()
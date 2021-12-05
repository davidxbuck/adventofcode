# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/3
#
import numpy as np

numbers = np.loadtxt('../inputs/Advent2021_03.txt', dtype=str)
numbers = np.array([list(map(int, list(x))) for x in numbers])
sums = np.sum(numbers, axis=0)
maxes = "".join(map(str, map(int, sums > numbers.shape[0]/2)))
mins = "".join(map(str, map(int, sums < numbers.shape[0]/2)))
print(f'Day 3, Part 1 {int(maxes, 2) * int(mins, 2)}')

generator = numbers.copy()
scrubber = numbers.copy()

for bit in range(numbers.shape[1]):
    generator = generator[generator[:, bit] == int(np.sum(generator[:, bit]) >= len(generator) / 2)]
    scrubber = scrubber[scrubber[:, bit] == int(np.sum(scrubber[:, bit]) < len(scrubber) / 2)]
    if len(generator) == 1:
        x = (int("".join(map(str, generator[0])), 2))
    if len(scrubber) == 1:
        y = (int("".join(map(str, scrubber[0])), 2))

print(f'Day 3, Part 2 {x * y}')

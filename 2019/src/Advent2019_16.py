# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/16
#
from itertools import cycle, repeat, islice
import numpy as np


def main():
    with open('../inputs/Advent2019_16.txt', 'r') as f:
        input_elements = np.array(list(map(int, list(f.readline().strip()))))
    elements = input_elements[:]
    pattern = [0, 1, 0, -1]
    # elements= np.array([1,2,3,4,5,6,7,8])
    num_elements = len(elements)


    positions = []
    for position in range(num_elements):
        repeater = [y  for x in pattern for y in list(repeat(x, position + 1))]
        positions.append(np.array(list(islice(cycle(repeater), 1, num_elements + 1))))

    for _ in range(100):
        output = []
        for iteration in range(num_elements):
            output.append(str(abs(np.sum(np.multiply(elements, positions[iteration])))%10))


        elements = np.array(list(map(int, list(output))))
        assert len(elements) == len(output)

    print(f'AoC 2019 Day 16, Part 1: {"".join(output)[:8]}')

    # elements= np.array([1,2,3,4,5,6,7,8])
    elements = input_elements[:] * 10000
    pattern = [0, 1, 0, -1]
    num_elements = len(elements)




    for turn in range(100):
        output = []
        for iteration in range(num_elements):
            repeater = [y for x in pattern for y in list(repeat(x, iteration + 1))][:num_elements]
            positions.append(np.array(list(islice(cycle(repeater), 1, num_elements + 1))))
            output.append(str(abs(np.sum(np.multiply(elements, positions[iteration])))%10))

            elements = np.array(list(map(int, list(output))))
        assert len(elements) == len(output)
        z = "".join(output)[:7]
        print(turn)
    print(z)
    z = int(z)
    print(elements[z: z+8])


if __name__ == '__main__':
    main()


from itertools import cycle, repeat, islice
import numpy as np


def main():
    with open('../inputs2019/Advent2019_16.txt', 'r') as f:
        elements = np.array(list(map(int, list(f.readline().strip()))))
    # elements= np.array([1,2,3,4,5,6,7,8])
    num_elements = len(elements)
    pattern = [0, 1, 0, -1]

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


if __name__ == '__main__':
    main()


# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/5
#
import matplotlib.pyplot as plt
import numpy as np

from Advent2019_Intcode import Intcode


def main():
    inputs = list(map(int, [code.strip().split(',') for code in open('../inputs2019/Advent2019_11.txt', 'r')][0]))

    grid, boolgrid = painting_robot(inputs, 0)
    plt.imshow(np.rot90(grid))
    plt.axis('off')
    plt.show()
    print(f'AoC 2019 Day 10, Part 1: {sum(sum(boolgrid))}')

    # print(f'\nAoC 2019 Day 9, Part 2: \n')
    # Intcode(inputs[:], inp=[2]).run()
    grid, boolgrid = painting_robot(inputs, 1)
    idx = np.argwhere(np.all(grid[..., :] == 0, axis=0))
    grid = np.delete(grid, idx, axis=1)
    plt.imshow(np.rot90(grid)[:, :45], )
    plt.axis('off')
    plt.show()


def painting_robot(inputs: list, start: int) -> (np.array, np.array):
    grid = np.zeros([50, 65], dtype=int)
    boolgrid = np.zeros([50, 65], dtype=bool)
    robot_pos = np.array([0, 20])
    robot_dir = 0
    directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
    terminated = False
    paint = Intcode(inputs[:], inp=[start], mode='run')
    while not terminated:
        colour, terminated = paint.run()
        grid[tuple(robot_pos)] = colour
        boolgrid[tuple(robot_pos)] = True
        direction, terminated = paint.run()
        if terminated:
            break
        if direction == 0:
            robot_dir -= 1
        elif direction == 1:
            robot_dir += 1
        else:
            raise ValueError
        robot_dir %= 4
        robot_pos += directions[robot_dir]
        paint.next_inp(grid[tuple(robot_pos)])
    return grid, boolgrid


if __name__ == '__main__':
    grid = main()

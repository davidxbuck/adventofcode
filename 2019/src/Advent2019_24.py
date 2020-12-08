# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/24
#

import numpy as np


def print_grid(bugs, level=None, recursive=False):
    if sum(bugs.flatten()) == 0:
        return
    if level is not None:
        print(f"\nLevel {level}\n")
    for i in range(5):
        for j in range(5):
            if recursive and i == 2 and j == 2:
                print('?', end=' ')
            elif bugs[i, j] == 0:
                print('.', end=' ')
            else:
                print('#', end=' ')
        print()
    print()


def main():
    with open('../inputs/Advent2019_24.txt', 'r') as f:
        # with open('../tests/test_Advent2019_24.txt', 'r') as f:
        inputs = [list(line.strip()) for line in f]
    bugs = np.array(inputs)
    bugs[bugs == '#'] = 1
    bugs[bugs == '.'] = 0
    bugs = bugs.astype(int)
    newbugs = np.zeros([7, 7], dtype=int)
    all_grids = [bugs.flatten().tobytes()]

    while True:

        newbugs[1:6, 1:6] = np.copy(bugs)

        for i in range(1, 6):
            for j in range(1, 6):
                neighbours = sum(newbugs[[i, i, i - 1, i + 1], [j - 1, j + 1, j, j]])
                bug = newbugs[i, j]
                if bug:
                    if neighbours != 1:
                        bugs[i - 1, j - 1] = 0

                else:
                    if neighbours in [1, 2]:
                        bugs[i - 1, j - 1] = 1

        # print_grid(bugs)
        flat = bugs.flatten().tobytes()
        output = 0
        if flat in all_grids:
            for x in range(25):
                if bugs.flatten()[x] == 1:
                    output += 2 ** x
            print(f"AoC 2019 Day 24, Part 1: {output}")
            break
        all_grids.append(flat)

    bugs = np.array(inputs)
    bugs[bugs == '#'] = 1
    bugs[bugs == '.'] = 0
    bugs = bugs.astype(int)

    dict_of_grids = {}
    maxdepth = 1
    dict_of_grids[0] = np.copy(bugs)
    dict_of_grids[1] = np.zeros([5, 5], dtype=int)
    dict_of_grids[-1] = np.zeros([5, 5], dtype=int)
    dict_of_grids[2] = np.zeros([5, 5], dtype=int)
    dict_of_grids[-2] = np.zeros([5, 5], dtype=int)

    for _ in range(200):
        updated_dict_of_grids = dict_of_grids.copy()
        for level in range(-maxdepth, maxdepth + 1):
            neighbours = [sum(dict_of_grids[level][[0, 1], [1, 0]]) + sum(dict_of_grids[level - 1][[1, 2], [2, 1]]),
                          sum(dict_of_grids[level][[0, 1, 0], [0, 1, 2]]) + dict_of_grids[level - 1][1, 2],
                          sum(dict_of_grids[level][[0, 1, 0], [1, 2, 3]]) + dict_of_grids[level - 1][1, 2],
                          sum(dict_of_grids[level][[0, 1, 0], [2, 3, 4]]) + dict_of_grids[level - 1][1, 2],
                          sum(dict_of_grids[level][[0, 1], [3, 4]]) + sum(dict_of_grids[level - 1][[1, 2], [2, 3]]),

                          sum(dict_of_grids[level][[0, 1, 2], [0, 1, 0]]) + dict_of_grids[level - 1][2, 1],
                          sum(dict_of_grids[level][[0, 1, 2, 1], [1, 0, 1, 2]]),
                          sum(dict_of_grids[level][[0, 1, 1], [2, 1, 3]]) + sum(dict_of_grids[level + 1][0, :]),
                          sum(dict_of_grids[level][[0, 1, 2, 1], [3, 2, 3, 4]]),
                          sum(dict_of_grids[level][[0, 1, 2], [4, 3, 4]]) + dict_of_grids[level - 1][2, 3],

                          sum(dict_of_grids[level][[1, 2, 3], [0, 1, 0]]) + dict_of_grids[level - 1][2, 1],
                          sum(dict_of_grids[level][[1, 2, 3], [1, 0, 1]]) + sum(dict_of_grids[level + 1][:, 0]),
                          0,
                          sum(dict_of_grids[level][[1, 2, 3], [3, 4, 3]]) + sum(dict_of_grids[level + 1][:, 4]),
                          sum(dict_of_grids[level][[1, 2, 3], [4, 3, 4]]) + dict_of_grids[level - 1][2, 3],

                          sum(dict_of_grids[level][[2, 3, 4], [0, 1, 0]]) + dict_of_grids[level - 1][2, 1],
                          sum(dict_of_grids[level][[2, 3, 4, 3], [1, 0, 1, 2]]),
                          sum(dict_of_grids[level][[3, 4, 3], [1, 2, 3]]) + sum(dict_of_grids[level + 1][4, :]),
                          sum(dict_of_grids[level][[2, 3, 4, 3], [3, 2, 3, 4]]),
                          sum(dict_of_grids[level][[2, 3, 4], [4, 3, 4]]) + dict_of_grids[level - 1][2, 3],

                          sum(dict_of_grids[level][[4, 3], [1, 0]]) + sum(dict_of_grids[level - 1][[3, 2], [2, 1]]),
                          sum(dict_of_grids[level][[4, 3, 4], [0, 1, 2]]) + dict_of_grids[level - 1][3, 2],
                          sum(dict_of_grids[level][[4, 3, 4], [1, 2, 3]]) + dict_of_grids[level - 1][3, 2],
                          sum(dict_of_grids[level][[4, 3, 4], [2, 3, 4]]) + dict_of_grids[level - 1][3, 2],
                          sum(dict_of_grids[level][[4, 3], [3, 4]]) + sum(dict_of_grids[level - 1][[3, 2], [2, 3]])]

            current_grid = np.copy(dict_of_grids[level])
            current_neighbour_grid = np.array(neighbours).reshape([5, 5])
            for i in range(5):
                for j in range(5):
                    bug = dict_of_grids[level][i, j]
                    neighbour = current_neighbour_grid[i, j]
                    if bug and neighbour != 1:
                        current_grid[i, j] = 0
                    elif not bug and neighbour in [1, 2]:
                        current_grid[i, j] = 1

            updated_dict_of_grids[level] = np.copy(current_grid)
        dict_of_grids = updated_dict_of_grids.copy()
        if sum(dict_of_grids[maxdepth].flatten()) + sum(dict_of_grids[-maxdepth].flatten()) > 0:
            maxdepth += 1
            dict_of_grids[maxdepth + 1] = np.zeros([5, 5], dtype=int)
            dict_of_grids[-maxdepth - 1] = np.zeros([5, 5], dtype=int)

    # for x in range(-maxdepth, maxdepth + 1):
    #     print_grid(dict_of_grids[x], x, recursive=True)

    print(
        f"AoC 2019 Day 24, Part 2: {sum(np.sum(np.sum(dict_of_grids[level])) for level in range(-maxdepth, maxdepth + 1))}")


if __name__ == '__main__':
    main()

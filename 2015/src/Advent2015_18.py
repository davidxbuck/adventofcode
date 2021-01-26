# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/18
#
import numpy as np

# Inputs
filename = ''
cubes = np.array(list(list(row.strip()) for row in open(f'../inputs/Advent2015_18{filename}.txt', 'r')))


def solve(cubes, part=1, loops=100, padding=1):
    # 2D
    array_size = [cubes.shape[0] + padding * 2, cubes.shape[1] + padding * 2]
    cube_grid = np.full(array_size, '.', dtype=str)
    cube_grid[padding:array_size[0] - padding, padding:array_size[1] - padding] = cubes.copy()
    x_corners = [1, array_size[0] - 2]
    y_corners = [1, array_size[1] - 2]
    for _ in range(loops):
        new_grid = np.full(array_size, '.', dtype=str)
        for x in range(1, array_size[0] - 1):
            for y in range(1, array_size[1] - 1):
                minicube = cube_grid[x - 1: x + 2, y - 1:y + 2]
                if (minicube[1, 1] == "#" and np.count_nonzero(minicube == "#") in [3, 4]) or (
                        minicube[1, 1] == "." and np.count_nonzero(minicube == "#") == 3):
                    new_grid[x, y] = "#"
                if part == 2 and x in x_corners and y in y_corners:
                    new_grid[x, y] = "#"
        cube_grid = new_grid
    return np.count_nonzero(cube_grid == "#")


print(f"""AoC 2015 Day 18 Part 1 answer is: {solve(cubes.copy(), part=1)}""")
print(f"""AoC 2015 Day 18 Part 1 answer is: {solve(cubes.copy(), part=2)}""")

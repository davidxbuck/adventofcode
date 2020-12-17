# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/17
#
import numpy as np

loops = 6
padding = loops + 1
printing = False
filename = ''

# Inputs
cubes = np.array(list(list(row.strip()) for row in open(f'../inputs/Advent2020_17{filename}.txt', 'r')))

# 3D
# Should really set the ranges so that each run only operates over x,y,z space that might contain #, and expand
array_size = [cubes.shape[0] + padding * 2, cubes.shape[1] + padding * 2, padding * 2 + 1]
cube_grid = np.full(array_size, '.', dtype=str)
cube_grid[padding:array_size[0] - padding, padding:array_size[1] - padding, padding] = cubes.copy()
for _ in range(loops):
    new_grid = np.full(array_size, '.', dtype=str)
    for x in range(1, array_size[0] - 1):
        for y in range(1, array_size[1] - 1):
            for z in range(1, array_size[2] - 1):
                minicube = cube_grid[x - 1: x + 2, y - 1:y + 2, z - 1: z + 2]
                if (minicube[1, 1, 1] == "#" and np.count_nonzero(minicube == "#") in [3, 4]) or (
                        minicube[1, 1, 1] == "." and np.count_nonzero(minicube == "#") == 3):
                    new_grid[x, y, z] = "#"
    cube_grid = new_grid

print(f"""AoC 2020 Day 17 Part 1 answer is: {np.count_nonzero(cube_grid == "#")}""")

# 4D
array_size = [cubes.shape[0] + padding * 2, cubes.shape[1] + padding * 2, padding * 2 + 1, padding * 2 + 1]
cube_grid = np.full(array_size, '.', dtype=str)
cube_grid[padding:array_size[0] - padding, padding:array_size[1] - padding, padding, padding] = cubes.copy()
for a in range(6):
    new_grid = np.full(array_size, '.', dtype=str)
    for x in range(1, array_size[0] - 1):
        for y in range(1, array_size[1] - 1):
            for z in range(1, array_size[2] - 1):
                for w in range(1, array_size[3] - 1):
                    minicube = cube_grid[x - 1: x + 2, y - 1:y + 2, z - 1: z + 2, w - 1: w + 2]
                    if (minicube[1, 1, 1, 1] == "#" and np.count_nonzero(minicube == "#") in [3, 4]) or (
                            minicube[1, 1, 1, 1] == "." and np.count_nonzero(minicube == "#") == 3):
                        new_grid[x, y, z, w] = "#"
    cube_grid = new_grid

print(f"""AoC 2020 Day 17 Part 2 answer is: {np.count_nonzero(cube_grid == "#")}""")

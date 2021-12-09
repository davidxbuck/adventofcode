# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/9
#
import numpy as np
import networkx as nx
import math

grid = np.array([list(map(int, list(row.strip()))) for row in open("../inputs/Advent2021_09.txt", "r")])
points = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])


def low_point(x, y):
    for point in points:
        check = tuple(np.array([x, y]) + point)
        if 0 <= check[0] < grid.shape[0] and 0 <= check[1] < grid.shape[1] and grid[check] <= grid[x, y]:
            return False
    return True


a = np.array([[low_point(x, y) for x in range(grid.shape[0])] for y in range(grid.shape[1])]).T
print(sum(grid[a] + 1))
print(f'Day 9, Part 1 {sum(grid[a] + 1)}')

G = nx.Graph()
for x in range(grid.shape[0] - 1):
    for y in range(grid.shape[1] - 1):
        if grid[x, y] != 9:
            if grid[x, y + 1] != 9:
                G.add_edge((x, y), (x, y + 1))
            if grid[x + 1, y] != 9:
                G.add_edge((x, y), (x + 1, y))

print(f'Day 9, Part 2 {math.prod(sorted([G.subgraph(c).number_of_nodes() for c in nx.connected_components(G)])[-3:])}')

# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/15
#
import numpy as np
import networkx as nx

grid = np.array([list(map(int, list(x))) for x in np.loadtxt('../inputs/Advent2021_15.txt', dtype=str)])
step_x, step_y = grid.shape


def create_digraph(grid):
    G = nx.DiGraph()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if y < grid.shape[0] - 1:
                G.add_edge((x, y), (x, y + 1), weight=grid[x, y + 1])
                G.add_edge((x, y + 1), (x, y), weight=grid[x, y])
            if x < grid.shape[1] - 1:
                G.add_edge((x, y), (x + 1, y), weight=grid[x + 1, y])
                G.add_edge((x + 1, y), (x, y), weight=grid[x, y])
    return G


G = create_digraph(grid)

path = nx.dijkstra_path(G, (0, 0), (step_x - 1, step_y - 1), weight='weight')
print(f"Day 15, Part 1: {nx.path_weight(G, path, 'weight')}")

grid_list = [grid.copy()]
for x in range(8):
    grid = grid_list[-1].copy()
    grid = grid + 1
    grid[grid > 9] = 1
    grid_list.append(grid)

grid = np.zeros((step_x * 5, step_y * 5), dtype=int)

for x in range(5):
    for y in range(5):
        step = x + y
        grid[x * step_x:(x + 1) * step_x, y * step_y:(y + 1) * step_y] = grid_list[x + y].copy()

G = create_digraph(grid)

path = nx.dijkstra_path(G, (0, 0), (grid.shape[0] - 1, grid.shape[1] - 1), weight='weight')
print(f"Day 15, Part 2: {nx.path_weight(G, path, 'weight')}")

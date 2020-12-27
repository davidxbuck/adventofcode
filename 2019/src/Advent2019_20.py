# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/20
#
from collections import defaultdict
import numpy as np
import networkx as nx

# Wrangle inputs into a num[y array
filename = ''
inputs = [row.rstrip("\n") for row in open(f'../inputs/Advent2019_20{filename}.txt', 'r')]
width = max(len(row) for row in inputs)
grid = np.array([list(f'{row:<{width}}') for row in inputs], dtype=str)

# Find all of the node names and locations

nodes = defaultdict(list)
inside_values = set()
for x in range(0, grid.shape[0] - 1):
    for y in range(0, grid.shape[1] - 1):
        if np.all(np.char.isalpha(grid[x:x + 2, y])):
            if x == 0:
                nodes["".join(grid[x:x + 2, y])] += [x + 2 + y * 1j]
            elif x == grid.shape[0] - 2:
                nodes["".join(grid[x:x + 2, y])] += [x - 1 + y * 1j]
            else:
                if x + 2 < grid.shape[0] and grid[x + 2, y] == ' ':
                    nodes["".join(grid[x:x + 2, y])] += [x - 1 + y * 1j]
                    inside_values.add(x - 1 + y * 1j)
                else:
                    nodes["".join(grid[x:x + 2, y])] += [x + 2 + y * 1j]
                    inside_values.add(x + 2 + y * 1j)
        if np.all(np.char.isalpha(grid[x, y:y + 2])):
            if y == 0:
                nodes["".join(grid[x, y:y + 2])] += [x + (y + 2) * 1j]
            elif y == grid.shape[1] - 2:
                nodes["".join(grid[x, y:y + 2])] += [x + (y - 1) * 1j]
            else:
                if y + 2 < grid.shape[1] and grid[x, y + 2] == ' ':
                    nodes["".join(grid[x, y:y + 2])] += [x + (y - 1) * 1j]
                    inside_values.add(x + (y - 1) * 1j)
                else:
                    nodes["".join(grid[x, y:y + 2])] += [x + (y + 2) * 1j]
                    inside_values.add(x + (y + 2) * 1j)

node_lookup = {x: k for k, v in nodes.items() for x in v}

# Create graph objct
G = nx.Graph()

for x in range(2, grid.shape[0] - 2):
    for y in range(2, grid.shape[1] - 2):
        if grid[x, y] == ".":
            current = x + 1j * y
            if grid[x - 1, y] == ".":
                G.add_edge(current, (x - 1) + 1j * y)
            if grid[x + 1, y] == ".":
                G.add_edge(current, (x + 1) + 1j * y)
            if grid[x, y - 1] == ".":
                G.add_edge(current, x + 1j * (y - 1))
            if grid[x, y + 1] == ".":
                G.add_edge(current, x + 1j * (y + 1))
            if current in node_lookup:
                matched = list(set(nodes[node_lookup[current]]) - {current})
                if matched:
                    G.add_edge(current, matched[0])

print(f"AoC 2019 Day 20, Part 1: {nx.shortest_path_length(G, nodes['AA'][0], nodes['ZZ'][0])}")

# Create graph. Connect inside portals to outside of new level until path found
G = nx.Graph()
offset = 0

while True:
    try:
        print(f"AoC 2019 Day 20, Part 2: {nx.shortest_path_length(G, nodes['AA'][0], nodes['ZZ'][0])}")
        print(f"Answer found at a recursion depth of {offset // 500}")
        break
    except (nx.exception.NetworkXNoPath, nx.exception.NodeNotFound):
        for x in range(2, grid.shape[0] - 2):
            for y in range(2, grid.shape[1] - 2):
                if grid[x, y] == ".":
                    current = x + 1j * y
                    if grid[x - 1, y] == ".":
                        G.add_edge(current + offset, (x - 1) + offset + 1j * y)
                    if grid[x + 1, y] == ".":
                        G.add_edge(current + offset, (x + 1) + offset + 1j * y)
                    if grid[x, y - 1] == ".":
                        G.add_edge(current + offset, x + offset + 1j * (y - 1))
                    if grid[x, y + 1] == ".":
                        G.add_edge(current + offset, x + offset + 1j * (y + 1))
                    if current in node_lookup:
                        if current in inside_values:
                            matched = list(set(nodes[node_lookup[current]]) - {current})
                            if matched:
                                G.add_edge(current + offset, matched[0] + offset + 500)
        offset += 500

# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/10
#
from collections import Counter
from math import prod

import networkx as nx
import numpy as np

adapters = np.sort(np.array(list(map(int, [row.strip() for row in open('../inputs/Advent2020_10.txt', 'r')]))))
adapters = np.insert(adapters, 0, 0., axis=0)
adapters = np.append(adapters, adapters[-1] + 3)
differences = adapters[1:] - adapters[:-1]
counts = Counter(differences)
print(f"AoC 2020 Day 10, Part 1 answer is {counts[1] * counts[3]}")

graphs = []
new = True

for ix, adapter in enumerate(adapters[:-1]):
    if new:
        graphs.append(nx.DiGraph())
    for x in range(1, 4):
        if ix + x > len(adapters) - 1 or adapters[ix + x] - adapter > 3:
            break
        graphs[-1].add_edge(adapter, adapters[ix + x])
        new = x == 1 and adapters[ix + x] - adapter == 3

paths = []
for graph in graphs:
    paths.append(len(list(nx.all_simple_paths(graph, min(graph.nodes), max(graph.nodes)))))

print(f"AoC 2020 Day 10, Part 1 answer is {prod(paths)}")

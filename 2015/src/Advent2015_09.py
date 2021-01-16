# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/9
import re
from itertools import permutations
from more_itertools import pairwise

import networkx as nx

data = [re.findall(r'^(\w+) to (\w+) = (\d+)', row.strip())[0] for row in open('../inputs/Advent2015_09.txt', 'r')]
G = nx.Graph()
for n1, n2, w in data:
    G.add_edge(n1, n2, weight=int(w))

min_len = 1e10
max_len = 0
for route in permutations(G.nodes, 8):
    length = sum(G.get_edge_data(x, y)['weight'] for x, y in pairwise(route))
    min_len = min(min_len, length)
    max_len = max(max_len, length)

print(f"AoC 2015 Day 9, Part 1 answer is {min_len}")
print(f"AoC 2015 Day 9, Part 2 answer is {max_len}")

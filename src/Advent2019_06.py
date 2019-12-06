# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/6
#
import networkx as nx

with open('../inputs2019/Advent2019_06.txt', 'r') as f:
    inputs = [line.strip().split(')') for line in f]

G = nx.Graph()
G.add_edges_from(inputs)

lengths = nx.shortest_path_length(G, source='COM')
print(f'AoC 2019 Day 1: {sum(lengths.values())}')

transfers = nx.shortest_path_length(G, source="YOU", target="SAN") - 2
print(f'AoC 2019 Day 2: {transfers}')
# Advent of Code 2017
#
# From https://adventofcode.com/2016/day/12
import re
import networkx as nx

G = nx.Graph()
nodes = set()
for x in (list(map(int, re.findall(r'\d+', row.strip()))) for row in open('../inputs/Advent2017_12.txt', 'r')):
    u = x[0]
    nodes.add(u)
    for v in x[1:]:
        G.add_edge(u, v)
        nodes.add(v)

print(f"AoC 2017 Day 12, Part 1: {len(nx.node_connected_component(G, 0))}")

groups = 0
while nodes:
    nodes = nodes - nx.node_connected_component(G, nodes.pop())
    groups += 1

print(f"AoC 2017 Day 12, Part 2: {groups}")

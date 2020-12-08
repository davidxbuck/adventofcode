# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/6
#
import matplotlib.pyplot as plt
import networkx as nx

with open('../inputs/Advent2019_06.txt', 'r') as f:
    inputs = [line.strip().split(')') for line in f]

G = nx.Graph()
G.add_edges_from(inputs)

lengths = nx.shortest_path_length(G, source='COM')
print(f'AoC 2019 Day 6 Part 1: {sum(lengths.values())}')

transfers = nx.shortest_path_length(G, source="YOU", target="SAN") - 2
print(f'AoC 2019 Day 6 Part 2: {transfers}')

plt.figure(figsize=(14, 14))
pos = nx.spring_layout(G)
nx.draw_networkx(G, node_size=4, pos=pos, font_size=6, arrows=False)
nx.draw_networkx(G.subgraph('COM'), pos=pos, node_size=180, node_color='black', font_size=6, font_color='yellow')
nx.draw_networkx(G.subgraph('YOU'), pos=pos, node_size=180, node_color='black', font_size=6, font_color='yellow')
nx.draw_networkx(G.subgraph('SAN'), pos=pos, node_size=180, node_color='black', font_size=6, font_color='yellow')
plt.show()

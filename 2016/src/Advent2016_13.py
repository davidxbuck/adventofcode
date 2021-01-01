# Advent of Code 2016
#
#  Interpreter
#
# From https://adventofcode.com/2020/day/13

import networkx as nx

FAVOURITE = 1350
G = nx.Graph()


def wall(node):
    x = node.real
    y = node.imag
    return f"{int(x * x + 3 * x + 2 * x * y + y + y * y + FAVOURITE):b}".count('1') % 2 == 1


for x in range(50):
    for y in range(50):
        node = x + 1j * y
        if not wall(node):
            east = node + 1
            if not wall(east):
                G.add_edge(node, east)
            south = node + 1j
            if not wall(south):
                G.add_edge(node, south)

print(f"AoC 2016 Day 13, Part 1 answer is {nx.shortest_path_length(G, 1 + 1j, 31 + 39j)} steps")

count = 0
for node in G.nodes:
    try:
        if nx.shortest_path_length(G, 1 + 1j, node) <= 50:
            count += 1
    except:
        pass

print(f"AoC 2016 Day 13, Part 2 answer is {count}")

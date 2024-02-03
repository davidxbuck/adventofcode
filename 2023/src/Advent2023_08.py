# Advent of Code 2023
#
# From https://adventofcode.com/2023/day/8
#
import math
import re
import itertools
import networkx as nx

left_right, path = open('../inputs/day8.txt', 'r').read().split('\n\n')
path = path.split('\n')
path = [re.findall(re.compile(r'([A-Z]+)'), x) for x in path]

G = nx.DiGraph()
nodes = []
for start, left, right in path:
    if start.endswith('A'):
        nodes.append(start)
    G.add_edge(start, left, weight='L')
    G.add_edge(start, right, weight='R')

node = 'AAA'
for count, lr in enumerate(itertools.cycle(left_right), 1):
    other_way = 'L' if lr == 'R' else 'R'
    paths = G.edges(node, data="weight")
    path = {node_lr: finish for start, finish, node_lr in paths}
    node = path.get(lr, path.get(other_way))
    if node == 'ZZZ':
        break
print(f'Day 8, Part 1 {count}')

# Brute Force Doesn't Work...
# for count, lr in enumerate(itertools.cycle(left_right), 1):
#     other_way = 'L' if lr == 'R' else 'R'
#     for ix, node in enumerate(nodes):
#         paths = G.edges(node, data="weight")
#         path = {node_lr: finish for start, finish, node_lr in paths}
#         nodes[ix] = path.get(lr, path.get(other_way))
#     if all(x.endswith('Z') for x in nodes):
#         break
# print(f'Day 8, Part 2 {count}')

positions = []
for ix, node in enumerate(nodes):
    for count, lr in enumerate(itertools.cycle(left_right), 1):
        other_way = 'L' if lr == 'R' else 'R'
        paths = G.edges(node, data="weight")
        path = {node_lr: finish for start, finish, node_lr in paths}
        node = path.get(lr, path.get(other_way))
        if node.endswith('Z'):
            positions.append(count)
            break
print(f'Day 8, Part 2 {math.lcm(*positions)}')
# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/12
#
import numpy as np
import networkx as nx
from queue import Queue

inp = [row.strip().split("-") for row in open("../inputs/Advent2021_12.txt", "r")]

G = nx.Graph()
for u, v in inp:
    G.add_edge(u, v)

Q = Queue()

Q.put(['start'])

is_lower = lambda x: x.lower() == x

result = []
visited = []

while not Q.empty():
    path_so_far = Q.get()
    neighbours = G.neighbors(path_so_far[-1])
    for neighbour in neighbours:
        next_path = path_so_far + [neighbour]
        if (neighbour.islower() and neighbour in path_so_far) or next_path in visited:
            continue
        visited.append(next_path)
        if neighbour == 'end':
            if next_path not in result:
                result.append(next_path)
        else:
            Q.put(next_path)
print(f'Day 12, Part 1 {len(result)}')

Q = Queue()

Q.put(['start'])

is_lower = lambda x: x.lower() == x

result = []
visited = []

while not Q.empty():
    path_so_far = Q.get()
    neighbours = G.neighbors(path_so_far[-1])
    for neighbour in neighbours:
        next_path = path_so_far + [neighbour]
        any_small_cave_visited_twice = any([path_so_far.count(x) == 2 for x in set(next_path) if is_lower(x)])
        if neighbour == 'start' or (
                neighbour != 'end' and neighbour.islower() and any_small_cave_visited_twice and path_so_far.count(
                neighbour) != 0) or next_path in visited:
            continue
        visited.append(next_path)
        if neighbour == 'end':
            if next_path not in result:
                result.append(next_path)
        else:
            Q.put(next_path)

print(f'Day 12, Part 2 {len(result)}')

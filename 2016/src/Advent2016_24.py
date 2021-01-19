# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/21
#
from itertools import product, permutations

import networkx as nx
import numpy as np
from more_itertools import pairwise

# Extract inputs
data = np.array([list(x.strip()) for x in open('../inputs/Advent2016_24.txt', 'r')])

G = nx.Graph()
numbers = {}
for y, x in product(range(data.shape[1] - 1), range(data.shape[0] - 1)):
    if data[x, y] == '#':
        continue
    if data[x + 1, y] != '#':
        G.add_edge(x + 1j * y, x + 1 + 1j * y)
    if data[x, y + 1] != '#':
        G.add_edge(x + 1j * y, x + 1j * (y + 1))
    if data[x, y].isdigit():
        numbers[data[x, y]] = x + 1j * y


def find_shortest(G, part=1):
    shortest = 999999999999
    numbers_list = list(numbers.values())
    zero = numbers_list.pop(numbers_list.index(numbers['0']))
    for order in permutations(numbers_list):
        length = 0
        if part == 1:
            order_zero = [zero] + list(order)
        else:
            order_zero = [zero] + list(order) + [zero]
        for a, b in pairwise(order_zero):
            length += nx.shortest_path_length(G, a, b)
        shortest = min(shortest, length)
    return shortest


print(f"AoC 2016 Day 24, Part 1 answer is {find_shortest(G, 1)}")
print(f"AoC 2016 Day 24, Part 2 answer is {find_shortest(G, 2)}")


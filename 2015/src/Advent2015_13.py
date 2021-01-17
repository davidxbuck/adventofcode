# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/13

import re
from itertools import permutations
from more_itertools import pairwise
import networkx as nx

data = [re.findall(r'^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).$', row.strip())[0] for row
        in
        open('../inputs/Advent2015_13.txt', 'r')]

data = [[x[0], x[3], -int(x[2])] if x[1] == 'lose' else [x[0], x[3], int(x[2])] for x in data]
names = {x[0] for x in data}

G = nx.DiGraph()


def find_best(names):
    best = -10000
    for row in permutations(names):
        row = list(row)
        row.append(row[0])
        happiness = 0
        for a, b in pairwise(row):
            c = G.get_edge_data(a, b)['weight']
            d = G.get_edge_data(b, a)['weight']
            happiness += c + d
        best = max(happiness, best)
    return best


for x, y, w in data:
    G.add_edge(x, y, weight=w)

print(f"AoC 2015 Day 13, Part 1 answer is {find_best(names)}")

for name in names:
    G.add_edge("Me", name, weight=0)
    G.add_edge(name, "Me", weight=0)
names.add("Me")

print(f"AoC 2015 Day 13, Part 2 answer is {find_best(names)}")

# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/7
#
import re
from collections import defaultdict

import networkx as nx


def get_bags(filename=''):
    inputs = [row.strip().split(' bags contain ') for row in open(f'../inputs2020/Advent2020_07{filename}.txt', 'r')]
    inputs = [[x[0], re.findall(r"^\s?(\d+|no) ([a-z]+ [a-z]+)", y)[0]] for x in inputs for y in x[1].split(',')]
    return inputs


bags = get_bags('')
G = nx.DiGraph()
innermost = []
target = 'shiny gold'

for outer_bag, inner_bag in bags:
    if outer_bag not in G:
        G.add_node(outer_bag)
    if inner_bag[0] != 'no':
        if inner_bag[1] not in G:
            G.add_node(inner_bag[1])
        G.add_edge(outer_bag, inner_bag[1], weight=int(inner_bag[0]))

innermost = [x for x in G.nodes() if G.out_degree(x) == 0 and G.in_degree(x) >= 1]
outermost = [x for x in G.nodes() if G.out_degree(x) >= 1 and G.in_degree(x) == 0]

target_bags = set()
for bag in outermost:

    paths = nx.all_simple_paths(G, bag, target)
    for path in paths:
        target_bags = target_bags.union(set(path))

total = 0
unprocessed = {target: 1}

while unprocessed:
    out = defaultdict(int)
    for bag, count in unprocessed.items():
        successors = list(G.successors(bag))
        for successor in successors:
            out[successor] += G.get_edge_data(bag, successor)['weight'] * count
            total += G.get_edge_data(bag, successor)['weight'] * count
    unprocessed = out

print(f"AoC 2015 Day 7, Part 1 answer is {len(target_bags) - 1}")
print(f"AoC 2015 Day 7, Part 2 answer is {total}")
# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/15

import re
from itertools import permutations
from more_itertools import pairwise
from math import prod
import networkx as nx

data = [re.findall(
    r'^(\w+): (capacity) (-?\d+), (durability) (-?\d+), (flavor) (-?\d+), (texture) (-?\d+), (calories) (-?\d+)$',
    row.strip())[0] for row in open('../inputs/Advent2015_15.txt', 'r')]

ingredients = {row[0]: {row[ix]: row[ix + 1] for ix in range(1, len(row), 2)} for row in data}

ingredient_list = list(ingredients.keys())


def sums(length, total_sum):
    if length == 1:
        yield total_sum,
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


summer = sums(len(ingredient_list), 100)
highest_500 = highest = 0
for nums in summer:
    total = []
    for x in ['capacity', 'durability', 'flavor', 'texture', 'calories']:
        quality = []
        for ix, stuff in enumerate(ingredient_list):
            quality.append(nums[ix] * int(ingredients[stuff][x]))
        quality = sum(quality)
        if quality < 0:
            quality = 0
        total.append(quality)
    calories = total.pop(4)
    highest = max(highest, prod(total))
    if calories == 500:
        highest_500 = max(highest_500, prod(total))

print(f"AoC 2015 Day 15, Part 1 answer is {highest}")
print(f"AoC 2015 Day 15, Part 2 answer is {highest_500}")

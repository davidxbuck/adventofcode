# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/21
#
import numpy as np
from math import prod
from collections import defaultdict, Counter

# Extract inputs
data = [x.strip().split(' (contains ') for x in open('../inputs/Advent2020_21.txt', 'r')]
ingredients = []
allergens = []
for row in data:
    ingredients.append(row[0].split(' '))
    allergens.append(row[1].strip(')').split(', '))

# Extract possible ingredients containing allergens
possible = {}
for ix, row in enumerate(allergens):
    for allergen in row:
        if allergen in possible:
            possible[allergen] = possible[allergen].intersection(set(ingredients[ix]))
        else:
            possible[allergen] = set(ingredients[ix])

# Sift known ingredients from possible ingredient containing allergens
actual = {}
while possible:
    for k, v in possible.items():
        if len(v) == 1:
            actual[k] = list(v)[0]
            del possible[k]
            for key in possible.keys():
                possible[key] = possible[key] - v
            break


all_allergens = list(actual[k] for k in sorted(actual.keys()))
all_ingredients = sum(ingredients, [])

print(f"AoC 2020 Day 21 Part 1: {sum(v for k, v in Counter(all_ingredients).items() if k not in all_allergens)}")
print(f"AoC 2020 Day 21 Part 2: {','.join(all_allergens)}")

# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/24
#
import numpy as np

# Extract rules
filename = ''
data = (x.strip() for x in open(f'../inputs/Advent2020_24{filename}.txt', 'r'))
rules = []
for row in data:
    parsed = []
    x = 0
    while x < len(row):
        if row[x] in ["e", "w"]:
            parsed.append(row[x])
            x += 1
        else:
            parsed.append(row[x:x + 2])
            x += 2
    rules.append(parsed)

floor = np.zeros((300, 300), dtype=int)

for rule in rules:
    x = y = 150
    for move in rule:
        if 'e' in move:
            if len(move) == 2:
                x += 1
            else:
                x += 2
        elif 'w' in move:
            if len(move) == 2:
                x -= 1
            else:
                x -= 2
        if move[0] == 'n':
            y += 1
        elif move[0] == 's':
            y -= 1
    floor[x, y] = 1 - floor[x, y]

print(f"""AoC 2020 Day 24 Part 1: {np.sum(np.sum(floor))}""")

maxx, maxy = floor.shape

for i in range(100):
    copy_floor = floor.copy()

    for x in range(2, maxx - 3):
        for y in range(x % 2 + 2, maxy - 3, 2):
            neighbours = sum(
                [floor[x - 1, y - 1], floor[x + 1, y - 1], floor[x - 1, y + 1], floor[x + 1, y + 1], floor[x - 2, y],
                 floor[x + 2, y]])
            if floor[x, y] == 1 and (neighbours == 0 or neighbours > 2):
                copy_floor[x, y] = 0
            elif floor[x, y] == 0 and neighbours == 2:
                copy_floor[x, y] = 1
    floor = copy_floor.copy()
    if filename:
        print(i + 1, np.sum(np.sum(floor)))

print(f"""AoC 2020 Day 24 Part 2: {np.sum(np.sum(floor))}""")

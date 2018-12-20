# Advent of Code 2018 Day 2

from collections import defaultdict, Counter
import re
import pandas as pd

# Data format example

# #1383 @ 720,683: 25x19
# #1384 @ 64,36: 23x24
# #1385 @ 735,608: 22x17
# #1386 @ 760,38: 25x17
file = open("Advent3.txt", 'r')
inputs = [row for row in file]
inpdata = []
for line in inputs:
    match = re.search(r'#(\d{1,}) @ (\d{1,}),(\d{1,}): (\d{1,})x(\d{1,})', line)
    inpdata.append(list(match.groups()))

df = pd.DataFrame(data=inpdata, columns=('index', 'x', 'y', 'width', 'height'), dtype=int)
df.set_index('index', inplace=True)
maxwidth = 1000
maxheight = 1000

# Check in case the width/height exceeds 1000 inches.
for i, row in df.iterrows():
    if row['x']+row['width'] > maxwidth: maxwidth = row['x']+row['width']
    if row['y']+row['height'] > maxheight: maxheight = row['y']+row['height']
print(maxwidth, maxheight)

# Create grid

blankgrid = [[ 0 for i in range(maxwidth)] for j in range(maxheight)]
grid = pd.DataFrame(data=blankgrid)
print(grid.head())

for i, row in df.iterrows():
    for x in range(row['x'], row['x']+row['width']):
        for y in range(row['y'], row['y']+row['height']):
            grid[x][y] += 1

count = grid.stack().value_counts()
print(type(count), count)

print("Part1: Sum of overlapping claims:", sum(list(count[2:])))

print(sum(count[2:]))

goodclaims = []
for i, row in df.iterrows():
    overlap = False
    for x in range(row['x'], row['x']+row['width']):
        for y in range(row['y'], row['y']+row['height']):
            if grid[x][y] > 1:
                overlap = True
                break
    if not overlap:
        goodclaims.append(i)

print("Part2: List of non-overlapping claims:", goodclaims)
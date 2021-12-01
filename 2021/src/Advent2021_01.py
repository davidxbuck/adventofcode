# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/1
#
import pandas as pd

depth_df = pd.DataFrame(map(int, (row.strip() for row in open('../inputs/Advent2021_01.txt', 'r'))), columns=['depth'])

print(f'AoC 2021 Day 1, Part 1 answer is {sum(depth_df.diff(axis=0)["depth"] > 0)}')
print(f'AoC 2021 Day 1, Part 2 answer is {sum(depth_df.rolling(window=3).sum().diff(axis=0)["depth"] > 0)}')

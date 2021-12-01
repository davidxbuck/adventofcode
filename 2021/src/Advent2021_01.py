# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/1
#
import pandas as pd

depth_df = pd.read_csv('../inputs/Advent2021_01.txt', names=["depth"])

print(f'Day 1, Part 1 {sum(depth_df.diff(axis=0)["depth"] > 0)}')
print(f'Day 1, Part 2 {sum(depth_df.rolling(window=3).sum().diff(axis=0)["depth"] > 0)}')

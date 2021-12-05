# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/2
#
import pandas as pd
import numpy as np

df = pd.read_csv('../inputs/Advent2021_02.txt', names=['direction', 'distance'], sep=' ')
df['part1_result'] = df['direction'].map({'forward': 1, 'down': 1j, 'up': -1j}) * df['distance']
final_position = df['part1_result'].sum()

print(f'Day 2, Part 1 {int(final_position.real * final_position.imag)}')

df['aim'] = (df['direction'].map({'forward': 0, 'down': 1, 'up': -1}) * df['distance']).cumsum()
df['part2_result'] = (real_result := np.real(df['part1_result'])) + real_result * df['aim'] * 1j
final_position2 = df['part2_result'].sum()
print(f'Day 2, Part 2 {int(final_position2.real * final_position2.imag)}')

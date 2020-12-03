# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/1
#
inputs = [data.strip() for data in open('../inputs2015/Advent2015_01.txt', 'r')][0]

print(f"AoC 2015 Day 1, Part 1 answer is {inputs.count('(')-inputs.count(')')}")

position = 0
for count, move in enumerate(inputs, 1):
    position += -1 * (move == ')') + 1 * (move == '(')
    if position == -1:
        print(f'AoC 2015 Day 1, Part 2 answer is {count}')
        break

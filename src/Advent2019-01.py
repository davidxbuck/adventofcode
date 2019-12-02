# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/1
#
masses = list(map(int, [mass.strip() for mass in open('../inputs2019/Advent2019-01.txt', 'r')]))
fuel = lambda x: x // 3 - 2
print(f'AoC 2019 Day 1, Part 1 answer is {sum(map(fuel, masses))}')

fuel_recursive = lambda x: x > 0 and (y := fuel(x)) + max(fuel_recursive(y), 0)
print(f'AoC 2019 Day 1, Part 2 answer is {sum(map(fuel_recursive, masses))}')

# One line answer... Might be slightly overlong for PEP-8
print(f'#1: {sum(map((fuel := lambda x: x // 3 - 2), (masses := list(map(int, [mass.strip() for mass in open("../inputs2019/Advent2019-01.txt", "r")])))))}\n#2: {sum(map((fuel_recursive := lambda x: x > 0 and (y := fuel(x)) + max(fuel_recursive(y), 0)), masses))}')

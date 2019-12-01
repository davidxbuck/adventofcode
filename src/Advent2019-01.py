# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/1
#
weights = list(map(int, [weight.strip() for weight in open('../inputs2019/Advent2019-01.txt', 'r')]))
fuelcalc = lambda x: x // 3 - 2
print(f'AoC 2019 Day 1, Part 1 answer is {sum(map(fuelcalc, weights))}')

fuel = lambda x: x > 0 and (y := fuelcalc(x)) + max(fuel(y), 0)
print(f'AoC 2019 Day 1, Part 2 answer is {sum(map(fuel, weights))}')

# One line answer... Might be slighly overlong for PEP-8
# print(f'AoC 2019 Day 1, Part 1 answer is {sum(map((fuelcalc := lambda x: x // 3 - 2), (weights := list(map(int, [weight.strip() for weight in open("../inputs2019/Advent2019-01.txt", "r")])))))}\nAoC 2019 Day 1, Part 2 answer is {sum(map((fuel := lambda x: x > 0 and (y := fuelcalc(x)) + max(fuel(y), 0)), weights))}')

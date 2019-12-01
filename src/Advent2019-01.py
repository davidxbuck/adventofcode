# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/1
#
weights = list(map(int, [weight.strip() for weight in open('../inputs2019/Advent2019-01.txt', 'r')]))
fuelcalc = lambda x : x//3 - 2
new_weights = list(map(fuelcalc, weights))
total_fuel = sum(new_weights)
print(f'AoC 2019 Day 1, Part 1 answer is {total_fuel}')

while sum(new_weights) > 0:
    new_weights = [x for x in list(map(fuelcalc, new_weights)) if x > 0]
    total_fuel += sum(new_weights)

print(f'AoC 2019 Day 1, Part 2 answer is {total_fuel}')
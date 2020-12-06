# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/6
#

data = [list(map(set, x.split('\n'))) for x in open('../inputs2020/Advent2020_06.txt', 'r').read().split('\n\n')]
print(f"""AoC 2020 Day 6 Part 1 answer is: {sum(len(set.union(*x)) for x in data)}""")
print(f"""AoC 2020 Day 6 Part 2 answer is: {sum(len(set.intersection(*x)) for x in data)}""")

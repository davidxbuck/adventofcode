# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/19
#

from queue import PriorityQueue

# Extract inputs
data = [x.strip().split(' => ') for x in open('../inputs/Advent2015_19.txt', 'r') if x.strip().split(' => ')[0]]
molecule = data.pop(-1)[0]

poss = set()

for change_from, change_to in data:
    for x in range(molecule.count(change_from)):
        poss.add(molecule.replace(change_from, "XXX", x).replace(change_from, change_to, 1).replace("XXX", change_from))

print(f"""AoC 2015 Day 19 Part 1 answer is: {len(poss)}""")

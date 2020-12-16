# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/16
#
import re
import numpy as np
from math import prod

# Extract inputs
data = [x.split('\n') for x in open('../inputs/Advent2020_16.txt', 'r').read().split('\n\n')]
all_fields = [re.findall(r'^(\w+\s?\w*): (\d+)-(\d+) or (\d+)-(\d+)$', entry)[0] for entry in data[0]]
fields = {x[0]: list(map(int, x[1:])) for x in all_fields}
fields_sets = {k: set(range(v[0], v[1] + 1)) | set(range(v[2], v[3] + 1)) for k, v in fields.items()}
my_ticket = list(map(int, data[1][1].split(',')))
nearby_tickets = [list(map(int, ticket.split(','))) for ticket in data[2][1:]]

# Validate Tickets
valid_set = set().union(*fields_sets.values())
print(f"""AoC 2020 Day 5 Part 1 answer is: {sum(sum([list(set(x) - valid_set) for x in nearby_tickets], []))}""")

# Valid tickets only
valid_array = np.array(nearby_tickets)[[set(x).issubset(valid_set) for x in nearby_tickets], :]
columns = [set().union(*[valid_array[:, y]]) for y in range(valid_array.shape[1])]

# Cross match fields and columns
result = {}
departure_fields = set([x for x in fields_sets.keys() if 'departure' in x])
while not departure_fields.issubset(set(result.keys())):
    for x, field in enumerate(fields_sets.keys()):
        cols = 0
        if field not in result.keys():
            for y, column in enumerate(columns):
                if y not in result.values() and column.issubset(fields_sets[field]):
                    poss_column = y
                    cols += 1
            if cols == 1:
                result[field] = poss_column

print(f"""AoC 2020 Day 5 Part 2 answer is: {prod(my_ticket[result[field]] for field in departure_fields)}""")

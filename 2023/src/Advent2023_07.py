# Advent of Code 2023
#
# From https://adventofcode.com/2023/day/7
#
from collections import Counter
sequence = {(5,): 7,
            (4, 1): 6,
            (3, 2): 5,
            (3, 1, 1): 4,
            (2, 2, 1): 3,
            (2, 1, 1, 1): 2,
            (1, 1, 1, 1, 1): 1
            }
data = [[ix] + x.split(' ') for ix, x in enumerate(open('../inputs/day7.txt', 'r').read().split('\n'))]
data = [[x, y, y.replace('T', chr(58)).replace('J', chr(59)).replace('Q', chr(60)).replace('K', chr(61)).replace('A', chr(62)), z] for x, y, z in data]
ranked = []
for a, b, c, d in data:
    rank = sequence[tuple(zip(*Counter(b).most_common()))[1]]
    ranked.append((rank, c, d))
sorted_data = sorted(ranked)
x = sum((ix * int(row[2])) for ix, row in enumerate(sorted_data, 1))
y = [(ix, int(row[2]), ix * int(row[2])) for ix, row in enumerate(sorted_data, 1)]
print(f'Day 4, Part 1 {x}')

data = [[ix] + x.split(' ') for ix, x in enumerate(open('../inputs/day7.txt', 'r').read().split('\n'))]
data = [[x, y, y.replace('T', chr(58)).replace('J', chr(47)).replace('Q', chr(60)).replace('K', chr(61)).replace('A', chr(62)), z] for x, y, z in data]
ranked = []
for a, b, c, d in data:
    if 'J' in b and b.count('J') != 5:
        rank = tuple(zip(*Counter(b).most_common()))
        b = b.replace('J', rank[0][0] if rank[0][0] != 'J' else rank[0][1])
    rank = sequence[tuple(zip(*Counter(b).most_common()))[1]]
    ranked.append((rank, c, d))
sorted_data = sorted(ranked)
x = sum((ix * int(row[2])) for ix, row in enumerate(sorted_data, 1))
y = [(ix, int(row[2]), ix * int(row[2])) for ix, row in enumerate(sorted_data, 1)]
print(f'Day 4, Part 2 {x}')

# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/14
#
from collections import Counter, defaultdict

data = [x.split('\n') for x in open(f'../inputs/Advent2021_14.txt', 'r').read().split('\n\n')]
template = data[0][0]
rules = dict(x.split(' -> ') for x in data[1])

pairs = Counter(template[x: x+2] for x in range(len(template) - 1))

for i in range(1, 41):
    out = defaultdict(int)
    for pair in pairs.keys():
        out[pair[0] + rules[pair][0]] += pairs[pair]
        out[rules[pair][0] + pair[1]] += pairs[pair]
    pairs = out
    if i == 10 or i == 40:
        counts = Counter()
        for k, v in pairs.items():
            counts[k[0]] += v
        counts[template[-1]] += 1
        print(f'Day 14, Part {int((i/10)**0.5)} {max(counts.values()) - min(counts.values())}')




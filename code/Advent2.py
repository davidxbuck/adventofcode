# Advent of Code 2018 Day 2

from collections import defaultdict, Counter


file = open("Advent2.txt", 'r')
inputs = [id[:-1] for id in file]

twos = 0
threes = 0

for x in inputs:        # For each ID code
    count = Counter()
    for y in x:
        count[y] += 1   # Create counter object for letters in ID

    inv_c = defaultdict(list)
    for k, v in count.items():   # Flip counter object
        inv_c[v].append(k)

    if len(inv_c[2]) > 0: twos += 1   # count ID containing twos or threes
    if len(inv_c[3]) > 0: threes += 1

print("Part1: Twos", twos, "Threes", threes, "Checksum", twos*threes)

length = len(inputs[0])
candidates = []
for idx, x in enumerate(inputs):
    for y in inputs[idx+1:]:
        if sum(x[z] == y[z] for z in range(length)) == length - 1:
            candidates.append(x)
            candidates.append(y)

answer = []
for x in range(length):
    if candidates[0][x] == candidates[1][x]: answer.append(candidates[0][x])

print("Part2: Common letters in target IDs", "".join(answer))







# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/4
from collections import Counter, defaultdict
import re
keys = [row.strip('\n]').split('[') for row in open('../inputs/Advent2016_04.txt', 'r')]

valid_count = 0
for key, code in keys:
    key_counts = Counter("".join(re.findall(r'[a-z]+', key)))
    sector_id = int(re.findall(r'\d+', key)[0])
    count_keys = defaultdict(list)
    for k, v in key_counts.items():
        count_keys[v] += k
    for k in count_keys.keys():
        count_keys[k] = sorted(count_keys[k])
    counter = 0
    valid = True
    for i in sorted(count_keys.keys(), reverse=True):
        if valid:
            for j in count_keys[i]:
                if counter >= 5:
                    break
                if j not in code:
                    valid = False
                    break
                counter += 1
    if valid:
        valid_count += sector_id

        out = ''
        for letter in key:
            if 97 <= ord(letter) <= 122:
                 out += chr((ord(letter) - 97 + sector_id) % 26 + 97)
            elif letter == '-':
                out += ' '
        if out.strip() == 'northpole object storage':
            print('AoC 2016 Day 4, Part 2 answer is ', sector_id)


print('AoC 2016 Day 4, Part 1 answer is ', valid_count)


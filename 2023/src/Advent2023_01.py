# Advent of Code 2023
#
# From https://adventofcode.com/2023/day/1
#

import re
from functools import reduce
data = [x for x in open('../inputs/day1.txt', 'r').read().split('\n')]
pattern = '(\d)'
print(f'Day 1, Part 1 {sum(int((y := re.findall(pattern, x))[0] + y[-1]) for x in data)}')
conversion = {'one': '1', 'two': '2', 'three':'3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

part2 = []
for z in data:
    y = 0
    aa = bb = z
    while y + 3 <= len(z):
        l = len(z)
        z = z[0: y] + reduce(lambda a, b: a.replace(b[0], b[1]), conversion.items(), z[y: y + 5]) + z[y + 5:]
        if l != len(z):
            break
        y += 1
    y = len(aa) - 3
    while y >= 0:
        l = len(aa)
        aa = aa[0: y] + reduce(lambda a, b: a.replace(b[0], b[1]), conversion.items(), aa[y: y + 5]) + aa[y + 5:]
        if l != len(aa):
            break
        y -= 1
    part2.append(int((re.findall(pattern, z))[0] + (re.findall(pattern, aa))[-1]))
print(f'Day 1, Part 2 {sum(part2)}')

# Much cleverer solution based on an idea from Reddit
conversion = {'one': 'o1e', 'two': 't2o', 'three':'th3ee', 'four': 'fo4r', 'five': 'fi5e', 'six': 's6x', 'seven': 'se7en', 'eight': 'ei8ht', 'nine': 'n9ne'}
print(f'Day 1, Part 2 (clever) {sum(int((re.findall(pattern, (z:=reduce(lambda a, b: a.replace(b[0], b[1]), conversion.items(), x))))[0] + (re.findall(pattern, z))[-1]) for x in data)}')
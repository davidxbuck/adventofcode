# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/12

import json
import re

filename = ''
data = [re.findall(r'(-?\d+)', row.strip()) for row in open(f'../inputs/Advent2015_12{filename}.json', 'r')]

print(f"AoC 2015 Day 12, Part 1 answer is {sum(int(x[0]) for x in data if x)}")

with open(f'../inputs/Advent2015_12{filename}.json', 'r') as read_file:
    data = json.load(read_file)


def parse_level(level):
    count = 0
    if isinstance(level, dict):
        if 'red' in level or 'red' in level.values():
            return 0
        for k, v in level.items():
            if isinstance(k, int) or isinstance(k, str) and k.isdigit():
                count += int(k)
            if isinstance(v, int) or isinstance(v, str) and v.isdigit():
                count += int(v)
            if isinstance(v, (dict, list)):
                count += parse_level(v)

    elif isinstance(level, list):
        for x in level:
            if isinstance(x, int) or isinstance(x, str) and x.isdigit():
                count += int(x)
            elif isinstance(x, (dict, list)):
                count += parse_level(x)

    return count


print(f"AoC 2015 Day 12, Part 2 answer is {parse_level(data)}")

# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/7
import re

addresses = [re.findall(r'\w+', row.strip()) for row in open('../inputs/Advent2016_07.txt', 'r')]


def palindrome_check(x):
    for y in range(0, len(x) - 3):
        if x[y] == x[y + 3] and x[y + 1] == x[y + 2] and x[y] != x[y + 1]:
            return True


valid_count = 0
for address in addresses:
    valid = False
    for x in address[::2]:
        if not valid:
            valid = palindrome_check(x)
    if valid:
        for x in address[1::2]:
            if palindrome_check(x):
                valid = False
                break
    if valid:
        valid_count += 1

print(f"AoC 2016 Day 7, Part 1 answer is {valid_count}")

valid_count = 0
for address in addresses:
    valid = False
    maybes = []
    for x in address[::2]:
        for y in range(len(x) - 2):
            if x[y] == x[y + 2] and x[y] != x[y + 1]:
                maybes.append(x[y + 1] + x[y] + x[y + 1])
    for y in address[1::2]:
        if any(z in y for z in maybes):
            valid = True
            break
    if valid:
        valid_count += 1
print(f"AoC 2016 Day 7, Part 2 answer is {valid_count}")

# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/7
import re

addresses = [re.findall(r'\w+', row.strip()) for row in open('../inputs/Advent2016_07.txt', 'r')]


def palindrome_check(substr):
    for y in range(0, len(substr) - 3):
        if substr[y] == substr[y + 3] and substr[y + 1] == substr[y + 2] and substr[y] != substr[y + 1]:
            return True
    return False


tls_count = 0
for address in addresses:
    valid = False
    for substring in address[::2]:
        if not valid:
            valid = palindrome_check(substring)
    if valid:
        for substring in address[1::2]:
            if palindrome_check(substring):
                valid = False
                break
    if valid:
        tls_count += 1

print(f"AoC 2016 Day 7, Part 1 answer is {tls_count}")

ssl_count = 0
for address in addresses:
    valid = False
    maybes = []
    for substring in address[::2]:
        for x in range(len(substring) - 2):
            if substring[x] == substring[x + 2] and substring[x] != substring[x + 1]:
                maybes.append(substring[x + 1] + substring[x] + substring[x + 1])
    for x in address[1::2]:
        if any(maybe in x for maybe in maybes):
            valid = True
            break
    if valid:
        ssl_count += 1
print(f"AoC 2016 Day 7, Part 2 answer is {ssl_count}")

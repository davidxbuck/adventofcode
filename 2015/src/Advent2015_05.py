# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/5
#

VOWELS = set('aeiou')
PAIRS = {x * 2 for x in 'abcdefghijklmnopqrstuvwxyz'}
NAUGHTY = {'ab', 'cd', 'pq', 'xy'}


def part1_check(string_):
    if sum(string_.count(v) for v in VOWELS) >= 3:
        pairs = set(string_[i:i + 2] for i in range(len(string_) - 1))
        if not pairs.intersection(NAUGHTY) and pairs.intersection(PAIRS):
            return True
    return False


def part2_check(string_):
    pair_check = any(string_.count(pair) >= 2 for pair in set(string_[i:i + 2] for i in range(len(string_) - 1)))
    skip_check = any(set(string_[i:i + 3:2] for i in range(len(string_) - 2)).intersection(PAIRS))
    return all((pair_check, skip_check))


inputs = [data.strip() for data in open('../inputs/Advent2015_05.txt', 'r')]
print(f"AoC 2015 Day 5, Part 1 answer is {sum(part1_check(x) for x in inputs)}")
print(f"AoC 2015 Day 5, Part 2 answer is {sum(part2_check(x) for x in inputs)}")

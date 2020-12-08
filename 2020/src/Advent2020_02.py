# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/2
#
import re

entries = (row.strip() for row in open('../inputs/Advent2020_02.txt', 'r'))
entry_list = [re.findall(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$", entry)[0] for entry in entries]

print(f"""AoC 2020 Day 2\n Part 1 answer is: {
sum(int(a) <= d.count(c) <= int(b) for a, b, c, d in entry_list)} \n Part 2 answer is: {
sum((d[int(a) - 1] == c) ^ (d[int(b) - 1] == c) for a, b, c, d in entry_list)}""")

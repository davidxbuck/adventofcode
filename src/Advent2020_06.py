# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/6
#
import string

def get_questionnaires(filename=''):
    answers = (set(row.strip()) for row in open(f'../inputs2020/Advent2020_06{filename}.txt', 'r'))

    part1 = part2 = 0
    part1_set, part2_set = set(), set(string.ascii_lowercase)
    for answer in answers:
        if answer:
            part1_set = part1_set.union(answer)
            part2_set = part2_set.intersection(answer)
        else:
            part1 += len(part1_set)
            part2 += len(part2_set)
            part1_set, part2_set = set(), set(string.ascii_lowercase)
    if answer:
        part1 += len(part1_set)
        part2 += len(part2_set)
    return part1, part2

part1, part2 = get_questionnaires()
print(f"""AoC 2020 Day 6 Part 1 answer is: {part1}""")
print(f"""AoC 2020 Day 6 Part 2 answer is: {part2}""")

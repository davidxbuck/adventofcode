# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/4
#
import re

START = 136760
STOP = 595730


def first_version():
    part1 = part2 = 0
    for i in range(START, STOP + 1):
        test = str(i)
        repeats = re.findall(r'(.)\1+', test)
        if repeats and test == "".join(sorted(test)):
            part1 += 1
            for repeat in repeats:
                if test.count(repeat) == 2:
                    part2 += 1
                    break
    print(f'AoC 2019 Day 4, Part 1: {part1}')
    print(f'AoC 2019 Day 4, Part 2: {part2}')


# For good measure (and borrowed initially from @brotherluii

def second_version():
    part1 = part2 = 0
    for number in range(START, STOP + 1):
        digits = str(number)
        adjacent = any(digits[i] == digits[i + 1] for i in range(5))
        is_increasing = adjacent and all(digits[i] <= digits[i + 1] for i in range(5))
        part1 += is_increasing
        doubles = is_increasing and any(digits.count(check) == 2 for check in set(digits))
        part2 += doubles
    print(f'AoC 2019 Day 4, Part 1: {part1}')
    print(f'AoC 2019 Day 4, Part 2: {part2}')


if __name__ == '__main__':
    first_version()
    second_version()

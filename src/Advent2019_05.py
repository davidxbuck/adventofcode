# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/5
#
from Advent2019_Intcode import Intcode


def main():
    inputs = list(map(int, [mass.strip().split(',') for mass in open('../inputs2019/Advent2019_05.txt', 'r')][0]))
    print(f'AoC 2019 Day 5, Part 1: \n')
    Intcode(inputs[:], inp=1).run()
    print(f'\nAoC 2019 Day 5, Part 2: \n')
    Intcode(inputs[:], inp=5).run()

if __name__ == '__main__':
    main()

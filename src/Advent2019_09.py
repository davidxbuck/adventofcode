# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/5
#
from Advent2019_Intcode import Intcode


def main():
    inputs = list(map(int, [code.strip().split(',') for code in open('../inputs2019/Advent2019_09.txt', 'r')][0]))
    # inputs = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    # inputs = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    # inputs = [104, 1125899906842624, 99]
    print(f'AoC 2019 Day 9, Part 1: \n')
    Intcode(inputs[:], inp=[1]).run()
    print(f'\nAoC 2019 Day 9, Part 2: \n')
    Intcode(inputs[:], inp=[2]).run()

if __name__ == '__main__':
    main()

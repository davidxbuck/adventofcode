# Advent of Code 2017
#
# From https://adventofcode.com/2017/day/6
#

class Distributor:
    def __init__(self):
        self.blocks = list(map(int, [row.strip().split('\t') for row in open('../inputs/Advent2017_06.txt', 'r')][0]))
        self.current = ""
        self.new = ""
        self.previous = set()
        self.count = 0

    def distribute(self):
        high = self.blocks.index(max(self.blocks))
        val = self.blocks[high]
        self.blocks[high] = 0
        for x in range(high + 1, high + 1 + val):
            self.blocks[x % len(self.blocks)] += 1
        self.count += 1
        return ".".join(map(str, self.blocks))

    def part1(self):
        while self.current not in self.previous:
            self.previous.add(self.current)
            self.current = self.distribute()
        return self.count

    def part2(self):
        self.count = 0
        while self.current != self.new:
            self.new = self.distribute()
        return self.count


def main():
    day6 = Distributor()
    print(f'AoC 2017 Day 6, Part 1 answer is {day6.part1()}')
    print(f'AoC 2017 Day 6, Part 2 answer is {day6.part2()}')


if __name__ == '__main__':
    main()

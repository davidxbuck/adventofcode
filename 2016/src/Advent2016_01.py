# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/1
#
from collections import deque


def part1(inp):
    q = deque([0 + 1j, 1, 0 - 1j, -1])
    position = 0 + 0j

    for move in inp:
        if len(move) >= 2:
            lr = move[0]
            dist = int(move[1:])
            q.rotate((lr == 'R') * 1 + (lr == 'L') * -1)
            position += q[0] * dist

    return int(abs(position.imag) + abs(position.real))


def part2(inp):
    q = deque([0 + 1j, 1, 0 - 1j, -1])
    position = 0 + 0j
    visited = set()
    visited.add(position)

    for move in inp:
        if len(move) >= 2:
            lr = move[0]
            dist = int(move[1:])
            q.rotate((lr == 'R') * 1 + (lr == 'L') * -1)
            for i in range(dist):
                position += q[0]
                if position in visited:
                    return int(abs(position.imag) + abs(position.real))
                else:
                    visited.add(position)


def main(filename=""):
    inp = [row.strip().split(', ') for row in open(f'../inputs2016/Advent2016_01{filename}.txt', 'r')][0]

    print(f"""AoC 2016 Day 1 Part 1 answer is: {part1(inp)}""")
    print(f"""AoC 2016 Day 1 Part 2 answer is: {part2(inp)}""")


if __name__ == '__main__':
    main()
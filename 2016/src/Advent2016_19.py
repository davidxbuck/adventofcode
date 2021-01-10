# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/19
from collections import deque

data = 3001330


def find_elf1(data):
    elves = {x: x + 1 for x in range(data)}
    elves[data - 1] = 0
    elf = 0
    while len(elves) > 1:
        to_del = elves[elf]
        elves[elf] = elves[elves[elf]]
        elf = elves[elf]
        del elves[to_del]
    return list(elves.values())[0] + 1


def find_elf2(data):
    q = deque()
    q.extend(range(1, data + 1))
    while len(q) > 1:
        x = len(q) // 2
        q.rotate(-x)
        q.popleft()
        q.rotate(x - 1)
    return q.pop()


print(f"AoC 2016 Day 19 Part 1 answer is: {find_elf1(data)}")
print(f"AoC 2016 Day 19 Part 2 answer is: {find_elf2(data)}")

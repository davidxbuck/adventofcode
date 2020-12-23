# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/23
#

from collections import deque

starting = "469217538"
# starting = "389125467"
cups = deque(list(map(int, starting)))


def move(q):
    current = q[0]
    q.rotate(-1)
    removed = [q.popleft() for _ in range(3)]
    remain = sorted(q)
    dest = remain[remain.index(current) - 1]
    [q.insert(q.index(dest) + pos, val) for pos, val in enumerate(removed, 1)]


for x in range(100):
    move(cups)

cups.rotate(-cups.index(1))

print(f"""AoC 2020 Day 23 Part 1: {"".join(list(map(str, list(cups))))[1:]}""")

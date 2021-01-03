# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/17
#
import hashlib
from queue import Queue


class Search:
    def __init__(self, inp, part=1):
        self.part = part
        self.searched = set()
        self.longest = 0
        self.inputs = inp
        self.q = Queue()
        self.q.put([1 + 1j, ""])
        self.pos = None
        self.key = None
        self.found = False
        self.direction = {"U": 0 - 1j,
                          "R": 1,
                          "D": 0 + 1j,
                          "L": -1
                          }
        self.so_far = None
        self.part1 = None

    def next_moves(self):
        self.pos, self.so_far = self.q.get()
        if self.pos == 4 + 4j:
            if self.part == 1:
                self.found = True
                return self.so_far
            else:
                self.longest = max([len(self.so_far), self.longest])
                return
        self.key = hashlib.md5(bytes(self.inputs + self.so_far, encoding='utf8')).hexdigest()
        for ix, direction in enumerate("UDLR"):
            if self.key[ix] in "bcdef":
                next_pos = self.pos + self.direction[direction]
                if 1 <= next_pos.real <= 4 and 1 <= next_pos.imag <= 4:
                    if self.so_far + direction not in self.searched:
                        self.searched.add(self.so_far + direction)
                    self.q.put((next_pos, self.so_far + direction))
        return

    def search(self):
        while not self.found and not self.q.empty():
            self.part1 = self.next_moves()
        if self.part == 1:
            return self.part1
        else:
            return self.longest


inputs = 'qtetzkpl'
# inputs = 'ihgpwlah'
# inputs = 'kglvqrro'
# inputs = 'ulqzkmiv'

search = Search(inputs, 1)
print(f"AoC 2016 Day 17 Part 1 answer is: {search.search()}")

search = Search(inputs, 2)
print(f"AoC 2016 Day 17 Part 2 answer is: {search.search()}")

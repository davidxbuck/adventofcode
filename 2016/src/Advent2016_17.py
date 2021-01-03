# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/17
#
import hashlib
from queue import Queue
from collections import defaultdict


class Search:
    def __init__(self):
        self.searched = set()
        self.prev = defaultdict(dict)
        self.inputs = 'qtetzkpl'
        # self.inputs = 'ihgpwlah'
        # self.inputs = 'kglvqrro'
        # self.inputs = 'ulqzkmiv'
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
        self.part1 = None
        self.sofar = None

    def next_moves(self):
        self.pos, self.sofar = self.q.get()
        last = 'S'
        if len(self.sofar) > 0:
            last = self.sofar[-1]
        if self.pos == 4 + 4j:
            self.found = True
            return self.sofar
        if self.pos in self.prev and last in self.prev[self.pos] and len(self.prev[self.pos][last]) < len(self.sofar):
            return
        self.prev[self.pos][last] = self.prev
        self.key = hashlib.md5(bytes(self.inputs + self.sofar, encoding='utf8')).hexdigest()
        for ix, dir in enumerate("UDLR"):
            if self.key[ix] in "bcdef":
                next_pos = self.pos + self.direction[dir]
                if 1 <= next_pos.real <= 4 and 1 <= next_pos.imag <= 4:
                    if self.sofar + dir not in self.searched:
                        self.searched.add(self.sofar + dir)
                        self.q.put((next_pos, self.sofar + dir))
        return

    def search(self):
        while not self.found and not self.q.empty():
            self.part1 = self.next_moves()
        return self.part1

search = Search()
print(search.search())
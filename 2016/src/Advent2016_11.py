# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/11
import re
from collections import defaultdict
from mendeleev import element
from itertools import combinations
import queue
import copy

FLOORS = ['first', 'second', 'third', 'fourth']


class Element:
    def __init__(self, name, thing):
        self.name = name
        self.thing = thing

    def __str__(self):
        return self.name + self.thing

    def __lt__(self, other):
        return self.name < other.name or (self.name == other.name and self.thing < other.thing)

    def __deepcopy__(self, memodict={}):
        return self

    def compatible(self, other):
        return self.name == other.name or self.thing == other.thing


class Building:
    def __init__(self, file):
        self.floors = defaultdict(list)
        self.moves = 0
        self.lift = 0
        data = [row.strip().split(' a ') for row in open(f'../inputs/Advent2016_11{file}.txt', 'r')]
        self.things = []
        for row in data:
            floor = FLOORS.index(re.findall(r'(first|second|third|fourth)', row[0])[0])
            for x in row[1:]:
                item, thing = (list(re.findall(r'(\w+).+(microchip|generator)', x)[0]))
                try:
                    item = element(item.title()).symbol
                except:
                    item = item.title()[:2]
                thing = thing[0].title()
                self.floors[floor].append(Element(item, thing))
                self.things.append(item + thing)
        self.things = sorted(self.things)

    def __str__(self):
        printout = []
        for floor in range(3, -1, -1):
            outfloor = [f"F{floor + 1}"]
            if self.lift == floor:
                outfloor.append('E')
            else:
                outfloor.append('.')
            for x in self.things:
                if any(str(y) == x for y in self.floors[floor]):
                    outfloor.append(x)
                else:
                    outfloor.append(' . ')
            printout.append(" ".join(outfloor))
        return "\n".join(printout)

    def __lt__(self, other):
        return self.priority < other.priority

    def possible_selections(self):
        self.poss_selection = []
        for x in self.floors[self.lift]:
            self.poss_selection.append([x])
        for x, y in combinations(self.floors[self.lift], 2):
            if x.compatible(y):
                self.poss_selection.append([x, y])

    def possible_directions(self):
        self.poss_directions = []
        if self.lift < 3:
            self.poss_directions.append(self.lift + 1)
        if self.lift > 0:
            self.poss_directions.append(self.lift - 1)

    def possible_moves(self):
        self.poss_moves = []
        self.possible_directions()
        self.possible_selections()
        for floor in self.poss_directions:
            for selection in self.poss_selection:
                if self.validate(self.floors[floor] + selection):
                    self.poss_moves.append([floor, selection])

    def validate(self, itemlist):
        itemlist = sorted(itemlist[:])
        reduced = itemlist[:]
        # print(f"Validating {[str(x) for x in sorted(itemlist)]}")
        for ix, item in enumerate(itemlist):
            if ix < len(itemlist) - 1 and item.name == itemlist[ix + 1].name and item.thing != itemlist[ix + 1].thing:
                reduced.pop(reduced.index(item))
                reduced.pop(reduced.index(itemlist[ix + 1]))
        # print("Reduced", [str(r) for r in reduced])
        things = [item.thing for item in reduced]
        # print("Things", [str(thing) for thing in things], not ('M' in things and 'G' in things))
        if 'M' in things and 'G' in things:
            return False
        else:
            return True

    @property
    def priority(self):
        return sum(len(x) * (3 - ix) for ix, x in enumerate(self.floors.values()))

    def move(self, next_move):
        self.moves += 1
        self.next_lift, self.to_move = next_move
        # print(f"\nBefore move \n{self.__str__()}, Lift at {self.lift+1}, Moves: {self.moves}")
        for x in self.to_move:
            popped = self.floors[self.lift].pop(self.floors[self.lift].index(x))
            self.floors[self.next_lift].append(popped)
        self.lift = self.next_lift
        # print(f"after move \n{self.__str__()}, Lift at {self.lift+1}, Moves: {self.moves}")

    @property
    def found(self):
        return all(len(self.floors[x]) == 0 for x in range(3))


class Search:
    def __init__(self, file=''):
        self.building = Building(file)
        print("\n Starting position")
        print(self.building)
        print()
        self.found = False
        self.q = queue.PriorityQueue()
        self.q.put((0, copy.deepcopy(self.building)))
        self.prev = set()

    def search(self):
        self.total = 0
        self.steps = 0
        while not self.found:
            _, self.current = self.q.get()
            self.total += 1
            if self.total % 100000 == 0:
                print(self.current)
            self.current.possible_moves()
            possible_moves = self.current.poss_moves
            if possible_moves:
                for next_move in possible_moves:
                    self.next = copy.deepcopy(self.current)
                    self.next.move(next_move)
                    if self.next.found:
                        self.found = True
                        break
                    if str(self.next) not in self.prev:
                        self.prev.add(str(self.next))
                        self.q.put((self.next.priority, copy.deepcopy(self.next)))
        print("\n Ending position")
        print(self.next)
        print()
        return self.next.moves


search = Search()
print(search.search(), search.total)
print(f"AoC 2016 Day 11, Part 1 answer is {search.search()}, search algorithm took {search.total} steps")

search = Search(file='b')
print(f"AoC 2016 Day 11, Part 2 answer is {search.search()}, search algorithm took {search.total} steps")

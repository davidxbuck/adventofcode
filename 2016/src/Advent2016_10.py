# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/10
import re
from collections import defaultdict
from math import prod

debug = False
data = [list(map(int, re.findall(r'\d+', row.strip()))) for row in open('../inputs/Advent2016_10.txt', 'r')]
botput = [re.findall(r'(bot|output)', row.strip()) for row in open('../inputs/Advent2016_10.txt', 'r')]


class Bot:
    def __init__(self, id_):
        self.id_ = id_
        self.chips = []
        self.queue = []

    @property
    def low(self):
        return min(self.chips)

    @property
    def high(self):
        return max(self.chips)

    @property
    def answer(self):
        return all(x in self.chips for x in [17, 61])

    @property
    def full(self):
        return len(self.chips) == 2

    @property
    def pending(self):
        return len(self.queue) > 0

    def pend(self, low, high):
        self.queue.append([low, high])

    def receive(self, val):
        self.chips.append(val)

    def execute(self):
        if self.pending and self.full:
            lo_bot, hi_bot = self.queue.pop()
            return_vals = [lo_bot, self.low, hi_bot, self.high]
            return return_vals


class Factory:
    def __init__(self):
        self.bots = defaultdict(Bot)
        self.answered = False

    def val_bot(self, id_):
        if isinstance(id_, int):
            id_ = [id_]
        for bot in id_:
            if bot not in self.bots:
                self.bots[bot] = Bot(bot)

    def give(self, bot, val):
        if debug:
            print(f"Instruction given to bot {bot} to receive {val}")
        self.val_bot(bot)
        self.bots[bot].receive(val)
        if self.bots[bot].answer:
            if not self.answered:
                print(f"AoC 2016 Day 10, Part 1 answer is {bot}")
                self.answered = True
        self.execute(bot)

    def instruct(self, bot, to_low, to_high):
        if debug:
            print(f"Instruction given to bot {bot} to move to {to_low}, {to_high}")
        self.bots[bot].pend(to_low, to_high)
        self.execute(bot)

    def execute(self, bot):
        if self.bots[bot].full and self.bots[bot].pending:
            lo_bot, low, hi_bot, high = self.bots[bot].execute()
            if debug:
                print(f"Bot {bot} moving {low} to {lo_bot} and {high} to {hi_bot}")
            self.give(lo_bot, low)
            self.give(hi_bot, high)
            if self.bots[bot].full and self.bots[bot].pending:
                self.execute(bot)


factory = Factory()

for ix, values in enumerate(data):
    if len(values) == 2:
        val, bot = values
        if botput[ix][0] == 'output':
            bot = bot + 1000
        factory.val_bot(bot)
        factory.give(bot, val)
    elif len(values) == 3:
        bot, hi, low = values
        if botput[ix][1] == 'output':
            hi = hi + 1000
        if botput[ix][2] == 'output':
            low = low + 1000
        factory.val_bot([bot, hi, low])
        factory.instruct(bot, hi, low)


print(f"AoC 2016 Day 10, Part 2 answer is {prod(factory.bots[bot].chips[0] for bot in range(1000, 1003))}")

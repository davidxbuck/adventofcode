# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/11
#
import math


class Monkey:
    def __init__(self, monkey_):
        self.number = int(monkey_[0].split(' ')[1].strip(':'))
        self.items = [Item(x) for x in map(int, monkey_[1].split(': ')[1].split(', '))]
        self.operation = monkey_[2].split(' = ')[1].replace('old', 'item.level')
        self.test_condition = int(monkey_[3].split(' ')[-1])
        self.if_true = int(monkey_[4].split(' ')[-1])
        self.if_false = int(monkey_[5].split(' ')[-1])
        self.count = 0

    def inspect(self, item):
        new = eval(self.operation)
        if divisor == 3:
            item.level = new // divisor
        else:
            item.level = new % divisor
        self.count += 1

    def test(self):
        while self.items:
            item = self.items.pop(0)
            self.inspect(item)
            if item.level % self.test_condition == 0:
                monkeys[self.if_true].items.append(item)
            else:
                monkeys[self.if_false].items.append(item)


class Item:
    def __init__(self, level):
        self.level = level


def reset_monkeys():
    monkeys_ = {}
    for monkey_ in data:
        new_monkey = Monkey(monkey_)
        monkeys_[new_monkey.number] = new_monkey
    return monkeys_


data = [x.split('\n') for x in open(f'../inputs/day11.txt', 'r').read().split('\n\n')]
monkeys = reset_monkeys()
divisor = 3
for x in range(20):
    for k, monkey in monkeys.items():
        monkey.test()

print(f'Day 11, Part 1 {math.prod(sorted(x.count for x in monkeys.values())[-2:])}')

monkeys = reset_monkeys()
divisor = math.prod([x.test_condition for x in monkeys.values()])
for x in range(10000):
    for k, monkey in monkeys.items():
        monkey.test()

print(f'Day 11, Part 2 {math.prod(sorted(x.count for x in monkeys.values())[-2:])}')

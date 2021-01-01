# Advent of Code 2016
#
#  Interpreter
#
# From https://adventofcode.com/2020/day/12

from collections import defaultdict


class Assembunny(object):
    def __init__(self, program, pointer=0, debug=False):
        self.debug = debug
        self.pointer = pointer
        self.program = defaultdict(list, enumerate(program[:]))
        self.terminated = False
        self.operation = None
        self.value = None
        self.registers = {x: 0 for x in range(4)}
        self.register_list = ['a', 'b', 'c', 'd']
        self.step = None

    def reg(self, reg):
        if reg in self.register_list:
            return self.register_list.index(reg)


    def int_or_reg(self, x):
        if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
            return int(x)
        else:
            return self.registers[self.reg(x)]

    def cpy(self, x):
        x, y = x
        # cpy x y copies x (either an integer or the value of a register) into register y.
        self.registers[self.reg(y)] = self.int_or_reg(x)
        self.pointer += 1

    def inc(self, x):
        # inc x increases the value of register x by one.
        x = x[0]
        self.registers[self.reg(x)] += 1
        self.pointer += 1

    def dec(self, x):
        # dec x decreases the value of register x by one.
        x = x[0]
        self.registers[self.reg(x)] -= 1
        self.pointer += 1

    def jnz(self, x):
        x, y = x
        # jnz x y jumps to an instruction y away (positive means forward; negative means backward),
        # but only if x is not zero.
        if self.int_or_reg(x) != 0:
            self.pointer += self.int_or_reg(y)
        else:
            self.pointer += 1

    def run(self):
        self.step = 1
        while not self.terminated:
            self.operation = self.program[self.pointer][0]
            self.value = self.program[self.pointer][1:]
            if self.debug:
                print(
                    f"Step:{self.step} Executing: Ptr:{self.pointer} Op:self.{self.operation}({self.value}) Registers: {self.registers}")
            exec(f"self.{self.operation}({self.value})")
            if self.pointer not in self.program:
                self.terminated = True
            self.step += 1


program = [row.strip().split() for row in open('../inputs/Advent2016_12.txt', 'r')]

part1 = Assembunny(program)
part1.run()
print(f"AoC 2016 Day 12, Part 1 answer is {part1.registers[0]}, program execution took {part1.step} steps")

part2 = Assembunny(program, debug=False)
part2.registers[2] = 1
part2.run()
print(f"AoC 2016 Day 12, Part 2 answer is {part2.registers[0]}, program execution took {part2.step} steps")

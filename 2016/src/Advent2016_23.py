# Advent of Code 2016
#
#  Interpreter
#
# From https://adventofcode.com/2020/day/23

from collections import defaultdict


class Assembunny(object):
    def __init__(self, prog, pointer=0, debug=False):
        self.debug = debug
        self.pointer = pointer
        self.program = defaultdict(list, enumerate(prog.copy()))
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
        if not y.isdigit():
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

    def tgl(self, x):
        # For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
        # For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
        # The arguments of a toggled instruction are not affected.
        # If an attempt is made to toggle an instruction outside the program, nothing happens.
        # If toggling produces an invalid instruction (like cpy 1 2) and an attempt is later made to execute that
        #   instruction, skip it instead.
        # If tgl toggles itself (for example, if a is 0, tgl a would target itself and become inc a),
        #   the resulting instruction is not executed until the next time it is reached.
        x = self.int_or_reg(x[0]) + self.pointer
        cmd = self.program.get(x)
        if cmd:
            if len(cmd) == 2:
                if cmd[0] == 'inc':
                    self.program[x][0] = 'dec'
                else:
                    self.program[x][0] = 'inc'
            elif len(cmd) == 3:
                if cmd[0] == 'jnz':
                    self.program[x][0] = 'cpy'
                else:
                    self.program[x][0] = 'jnz'
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


program = [row.strip().split() for row in open('../inputs/Advent2016_23.txt', 'r')]
part1 = Assembunny(program.copy())
part1.registers[0] = 12
part1.run()
print(f"AoC 2016 Day 23, Part 1 answer is {part1.registers[0]}, program execution took {part1.step} steps")
#
# part2 = Assembunny(program.copy())
# part2.registers[0] = 7
# part2.run()
# print(f"AoC 2016 Day 23, Part 2 answer is {part2.registers[0]}, program execution took {part2.step} steps")

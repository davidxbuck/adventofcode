# Advent of Code 2019
#
# Intcode Interpreter
#
# From https://adventofcode.com/2019/day/2
#

class Intcode(object):
    def __init__(self, program, noun=0, verb=0, pointer=0):
        self.pointer = pointer
        self.program = program
        self.program[1:3] = noun, verb
        self.terminated = False

    def cmd1(self):
        cmd, augend, addend, sum_ = self.program[self.pointer:self.pointer + 4]
        self.program[sum_] = self.program[augend] + self.program[addend]

    def cmd2(self):
        multiplicand, multiplier, product = self.program[self.pointer + 1:self.pointer + 4]
        self.program[product] = self.program[multiplicand] * self.program[multiplier]

    def cmd99(self):
        self.terminated = True

    def run(self):
        while not self.terminated:
            # print(f"Executing: {self.pointer} {self.program[self.pointer:self.pointer + 4]}")
            exec(f"self.cmd{self.program[self.pointer]}()")
            if not self.terminated:
                self.pointer += 4
        return self.program[0]
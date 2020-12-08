# Advent of Code 2020
#
#  Interpreter
#
# From https://adventofcode.com/2020/day/8

from collections import defaultdict
class Machine(object):
    def __init__(self, program, pointer=0, accumulator=0, mode=None, debug=False):
        self.debug = debug
        self.mode = mode
        self.accumulator = accumulator
        if self.accumulator is None:
            self.accumulator = 0
        self.pointer = pointer
        self.program = defaultdict(list, enumerate(program))
        self.terminated = False
        self.diagnostic = debug
        self.operation = None
        self.value = None

    def nop(self):
        self.pointer += 1

    def jmp(self):
        self.pointer += self.value

    def acc(self):
        self.accumulator += self.value
        self.pointer += 1

    def run(self):
        step = 1
        while not self.terminated:
            self.operation = self.program[self.pointer][0]
            self.value = self.program[self.pointer][1]
            if self.debug:
                print(f"Step:{step} Executing: Ptr:{self.pointer} Op:self.{self.operation}() Value:{self.accumulator} Mode={self.mode}")
            if self.mode == 1:
                if self.operation == 'jmp' and not (0 <= self.pointer + self.value < len(self.program)):
                    self.terminated = True
                    if self.debug:
                        print("Terminated - program complete")
                    return False, self.accumulator
                if self.operation == 'jmp' and self.program[self.pointer + self.value][2] is True:
                    self.terminated = True
                    if self.debug:
                        print("Terminated - loop found")
                    return True, self.accumulator
            self.program[self.pointer][2] = True
            exec(f"self.{self.operation}()")
            if self.mode == 1:
                if self.pointer >= len(self.program):
                    self.terminated = True
                    print("Terminated - program complete")
                    return False, self.accumulator
            step += 1

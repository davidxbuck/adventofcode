# Advent of Code 2019
#
# Intcode Interpreter
#
# From https://adventofcode.com/2019/day/2
# From https://adventofcode.com/2019/day/5

class Intcode(object):
    def __init__(self, program, noun=-1, verb=-1, pointer=0, inp=0):
        self.pointer = pointer
        self.program = program
        if noun > 0 and verb > 0:
            self.program[1:3] = noun, verb
        self.terminated = False
        self.inp = inp

    @property
    def parameters(self):
        return any((self.parm3, self.parm2, self.parm1))

    def cmd01(self):
        augend_val = self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]]
        addend_val = self.program[self.pointer + 2] if self.parm2 else self.program[self.program[self.pointer + 2]]
        sum_       = self.program[self.pointer + 3]
        self.program[sum_] = augend_val + addend_val
        self.pointer += 4

    def cmd02(self):
        multiplicand_val = self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]]
        multiplier_val   = self.program[self.pointer + 2] if self.parm2 else self.program[self.program[self.pointer + 2]]
        product          = self.program[self.pointer + 3]
        self.program[product] = multiplicand_val * multiplier_val
        self.pointer += 4

    def cmd03(self):
        self.program[self.program[self.pointer + 1]] = self.inp
        self.pointer += 2


    def cmd04(self):
        out = self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]]
        print(f"Diagnostic Code: {out}")
        self.pointer += 2

    def cmd05(self):
        jump_if_true  = self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]]
        jump          = self.program[self.pointer + 2] if self.parm2 else self.program[self.program[self.pointer + 2]]
        if jump_if_true:
            self.pointer = jump
        else:
            self.pointer += 3

    def cmd06(self):
        jump_if_false  = not(self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]])
        jump          = self.program[self.pointer + 2] if self.parm2 else self.program[self.program[self.pointer + 2]]
        if jump_if_false:
            self.pointer = jump
        else:
            self.pointer += 3

    def cmd07(self):
        val1 = self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]]
        val2 = self.program[self.pointer + 2] if self.parm2 else self.program[self.program[self.pointer + 2]]
        out  = self.program[self.pointer + 3]
        self.program[out] = 1 if val1 < val2 else 0
        self.pointer += 4

    def cmd08(self):
        val1 = self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]]
        val2 = self.program[self.pointer + 2] if self.parm2 else self.program[self.program[self.pointer + 2]]
        out  = self.program[self.pointer + 3]
        self.program[out] = 1 if val1 == val2 else 0
        self.pointer += 4

    def cmd99(self):
        self.terminated = True

    def run(self):
        while not self.terminated:
            operation = f'{self.program[self.pointer]:>05}'
            # print(f"Executing: {self.pointer} {operation} {self.program[self.pointer:self.pointer + 4]}")
            self.parm3, self.parm2, self.parm1 = map(int, tuple(operation[0:3]))
            self.opcode = operation[3:5]
            exec(f"self.cmd{self.opcode}()")
        return self.program[0]
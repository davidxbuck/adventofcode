# Advent of Code 2019
#
# Intcode Interpreter
#
# From https://adventofcode.com/2019/day/2
# From https://adventofcode.com/2019/day/5
# From https://adventofcode.com/2019/day/7

class Intcode(object):
    def __init__(self, program, noun=-1, verb=-1, pointer=0, inp=[0], mode='diagnostic'):
        if inp is None:
            inp = [0]
        self.pointer = pointer
        self.program = program
        if noun > 0 and verb > 0:
            self.program[1:3] = noun, verb
        self.terminated = False
        self.inp = inp
        self.inp_pos = 0
        self.diagnostic = True if mode=='diagnostic' else False
        self.output = -1
    def next_inp(self, inp):
        self.inp.append(inp)

    def get_vals(self):
        val1 = self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]]
        val2 = self.program[self.pointer + 2] if self.parm2 else self.program[self.program[self.pointer + 2]]
        return val1, val2

    def get_val3(self):
        return self.program[self.pointer + 3]

    def cmd01(self):
        val1, val2 = self.get_vals()
        self.program[self.get_val3()] = val1 + val2
        self.pointer += 4

    def cmd02(self):
        val1, val2 = self.get_vals()
        self.program[self.get_val3()] = val1 * val2
        self.pointer += 4

    def cmd03(self):
        self.program[self.program[self.pointer + 1]] = self.inp[self.inp_pos]
        # print(f'Input received {self.inp[self.inp_pos]}')
        self.inp_pos += 1
        self.pointer += 2

    def cmd04(self):
        out = self.program[self.pointer + 1] if self.parm1 else self.program[self.program[self.pointer + 1]]
        if self.diagnostic:
            print(f"Diagnostic Code: {out}")
        else:
            self.output = out
        self.pointer += 2

    def cmd05(self):
        jump_if_true, jump = self.get_vals()
        if jump_if_true:
            self.pointer = jump
        else:
            self.pointer += 3

    def cmd06(self):
        dont_jump_if_true, jump = self.get_vals()
        if not dont_jump_if_true:
            self.pointer = jump
        else:
            self.pointer += 3

    def cmd07(self):
        val1, val2 = self.get_vals()
        self.program[self.get_val3()] = 1 if val1 < val2 else 0
        self.pointer += 4

    def cmd08(self):
        val1, val2 = self.get_vals()
        self.program[self.get_val3()] = 1 if val1 == val2 else 0
        self.pointer += 4

    def cmd99(self):
        self.terminated = True

    def run(self):
        while not self.terminated:
            operation = f'{self.program[self.pointer]:05}'
            # print(f"Executing: {self.pointer} {operation} {self.program[self.pointer:self.pointer + 4]}")
            self.parm3, self.parm2, self.parm1 = map(int, (operation[0:3]))
            self.opcode = operation[3:5]
            exec(f"self.cmd{self.opcode}()")
            if self.output != -1:
                out = self.output
                self.output = -1
                return out, self.terminated
        return self.program[0], self.terminated

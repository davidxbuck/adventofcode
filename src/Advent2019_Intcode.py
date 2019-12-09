# Advent of Code 2019
#
# Intcode Interpreter
#
# From https://adventofcode.com/2019/day/2
# From https://adventofcode.com/2019/day/5
# From https://adventofcode.com/2019/day/7
# From https://adventofcode.com/2019/day/9


class Intcode(object):
    def __init__(self, program, noun=-1, verb=-1, pointer=0, inp=[0], mode='diagnostic'):
        if inp is None:
            inp = [0]
        self.pointer = pointer
        self.program = program + [0] * 1000
        if noun > 0 and verb > 0:
            self.program[1:3] = noun, verb
        self.terminated = False
        self.inp = inp
        self.inp_pos = 0
        self.diagnostic = True if mode.lower() == 'diagnostic' else False
        self.test = True if mode.lower() == 'test' else False
        self.output = -1
        self.relative_base = 0

    @property
    def parameters(self):
        return (self.parm1, self.parm2, self.parm3)

    def next_inp(self, inp):
        self.inp.append(inp)

    def get_vals(self, count):
        retvals = []
        for i in range(count):
            if self.parameters[i] == 0:
                retvals.append(self.program[self.program[self.pointer + i + 1]])
            elif self.parameters[i] == 1:
                retvals.append(self.program[self.pointer + i + 1])
            elif self.parameters[i] == 2:
                retvals.append(self.program[self.program[self.pointer + i + 1] + self.relative_base])
            else:
                raise ValueError
        if len(retvals) == 1:
            return retvals[0]
        else:
            return retvals

    def get_val3(self):
        if self.parm3 == 0:
            return self.program[self.pointer + 3]
        elif self.parm3 == 2:
            return self.program[self.pointer + 3] + self.relative_base
        else:
            raise ValueError

    def cmd01(self):
        val1, val2 = self.get_vals(2)
        self.program[self.get_val3()] = val1 + val2
        self.pointer += 4

    def cmd02(self):
        val1, val2 = self.get_vals(2)
        self.program[self.get_val3()] = val1 * val2
        self.pointer += 4

    def cmd03(self):
        if self.parm1 == 0:
            self.program[self.program[self.pointer + 1]] = self.inp[self.inp_pos]
        elif self.parm1 == 2:
            self.program[self.program[self.pointer + 1] + self.relative_base] = self.inp[self.inp_pos]
        else:
            raise ValueError
        # print(f'Input received {self.inp[self.inp_pos]}')
        self.inp_pos += 1
        self.pointer += 2

    def cmd04(self):
        out = self.get_vals(1)
        if self.diagnostic:
            print(f"Diagnostic Code: {out}")
        elif self.test:
            try:
                self.testout.append(out)
            except:
                self.testout = [out]
        else:
            self.output = out
        self.pointer += 2

    def cmd05(self):
        jump_if_true, jump = self.get_vals(2)
        if jump_if_true:
            self.pointer = jump
        else:
            self.pointer += 3

    def cmd06(self):
        dont_jump_if_true, jump = self.get_vals(2)
        if not dont_jump_if_true:
            self.pointer = jump
        else:
            self.pointer += 3

    def cmd07(self):
        val1, val2 = self.get_vals(2)
        self.program[self.get_val3()] = 1 if val1 < val2 else 0
        self.pointer += 4

    def cmd08(self):
        val1, val2 = self.get_vals(2)
        self.program[self.get_val3()] = 1 if val1 == val2 else 0
        self.pointer += 4

    def cmd09(self):
        val1 = self.get_vals(1)
        self.relative_base += val1
        self.pointer += 2

    def cmd99(self):
        self.terminated = True

    def run(self):
        while not self.terminated:
            operation = f'{self.program[self.pointer]:05}'
            # print(f"Executing: Ptr:{self.pointer} Offset:{self.relative_base} Op:{operation} Vals:{self.program[self.pointer:self.pointer + 4]} {self.program}")
            self.parm3, self.parm2, self.parm1 = map(int, (operation[0:3]))
            self.opcode = operation[3:5]
            exec(f"self.cmd{self.opcode}()")
            if self.output != -1:
                out = self.output
                self.output = -1
                return out, self.terminated
        if self.test:
            return self.testout
        else:
            return self.program[0], self.terminated

class Registers(object):

    def __init__(self, values):
        self.registers = values[:]
        self.opcode = None
        self.inputA = None
        self.inputB = None
        self.output = None

    def set_registers(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC

    #
    # Addition:
    # addr (add register) stores into register C the result of adding register A and register B.
    def addr(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)

        self.registers[self.output] = self.registers[self.inputA] + self.registers[self.inputB]

    # addi (add immediate) stores into register C the result of adding register A and value B.
    def addi(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.registers[self.inputA] + self.inputB

    #
    # Multiplication:
    # mulr (multiply register) stores into register C the result of multiplying register A and register B.
    def mulr(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.registers[self.inputA] * self.registers[self.inputB]

    # muli (multiply immediate) stores into register C the result of multiplying register A and value B.
    def muli(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.registers[self.inputA] * self.inputB

    #
    # Bitwise AND:
    # banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
    def banr(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.registers[self.inputA] & self.registers[self.inputB]

    # bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
    def bani(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.registers[self.inputA] & self.inputB

    #
    # Bitwise OR:
    # borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
    def borr(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.registers[self.inputA] | self.registers[self.inputB]

    # bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
    def bori(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.registers[self.inputA] | self.inputB

    #
    # Assignment:
    # setr (set register) copies the contents of register A into register C. (Input B is ignored.)
    def setr(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.registers[self.inputA]

    # seti (set immediate) stores value A into register C. (Input B is ignored.)
    def seti(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = self.inputA

    #
    # Greater-than testing:
    # gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
    def gtir(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = 1 if self.inputA > self.registers[self.inputB] else 0

    # gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
    def gtri(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = 1 if self.registers[self.inputA] > self.inputB else 0

    # gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
    def gtrr(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = 1 if self.registers[self.inputA] > self.registers[self.inputB] else 0

    #
    # Equality testing:
    # eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
    def eqir(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = 1 if self.inputA == self.registers[self.inputB] else 0

    # eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
    def eqri(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = 1 if self.registers[self.inputA] == self.inputB else 0

    # eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
    def eqrr(self, opcode, inputA, inputB, outputC):
        self.set_registers(opcode, inputA, inputB, outputC)
        self.registers[self.output] = 1 if self.registers[self.inputA] == self.registers[self.inputB] else 0


def read_program(advent_):
    file = open("../inputs/%s" % advent_, 'r')
    bound = int(next(file)[4])
    print("Part 1 - Instructions are bound to register {}".format(bound))
    # Extract program into dict
    inputs = [row.strip("\n").split(' ') for row in file]
    program = dict(enumerate([row[:1] + [int(x) for x in row[1:]] for row in inputs]))
    return bound, program
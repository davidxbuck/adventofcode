# Advent of Code 2018 Day 19
#
#
#
from AdventMachine import Registers, read_program


def main():
    advent_ = "Advent19"
    bound, program = read_program(advent_)

    # Run program

    ip = 0
    opcode = 0  # Has no effect on operations
    x = Registers([0, 0, 0, 0, 0, 0])

    while ip < len(program):
        x.registers[bound] = ip
        operator, inputA, inputB, outputC = program[ip]
        exec("x.{}(opcode, inputA, inputB, outputC)".format(operator))
        ip = x.registers[bound] + 1

    print("Part 1 - Final result after all commands run", x.registers)


if __name__ == "__main__":
    main()

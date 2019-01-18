# Advent of Code 2018 Day 21
#
#
#
from AdventMachine import Registers, read_program


def main():
    advent_ = "Advent21"
    bound, program = read_program(advent_)

    # Run program

    ip = 0
    opcode = 0  # Has no effect on operations
    x = Registers([2985446, 0, 0, 0, 0, 0])

    y = 0
    while ip < len(program):
        if ip == 28:
            break
        x.registers[bound] = ip
        operator, inputA, inputB, outputC = program[ip]
        exec("x.{}(opcode, inputA, inputB, outputC)".format(operator))

        ip = x.registers[bound] + 1
    print("Part 1 - First value of x that will cause the program to stop", x.registers[4])


if __name__ == "__main__":
    main()

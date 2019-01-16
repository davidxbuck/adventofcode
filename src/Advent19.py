# Advent of Code 2018 Day 19
#
#
#
from AdventMachine import Registers


def main():
    file = open("../inputs/Advent19", 'r')
    bound = int(next(file)[4])
    print("Part 1 - Instructions are bound to register {}".format(bound))

    # Extract program into dict
    inputs = [row.strip("\n").split(' ') for row in file]
    program = dict(enumerate([row[:1] + [int(x) for x in row[1:]] for row in inputs]))

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

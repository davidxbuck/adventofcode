# Advent of Code 2018 Day 21
#
#
#
from AdventMachine import Registers, read_program
opcode = 0  # Has no effect on operations


def execute(bound, ip, program, x):
    x.registers[bound] = ip
    operator, inputA, inputB, outputC = program[ip]
    exec("x.{}(opcode, inputA, inputB, outputC)".format(operator))
    ip = x.registers[bound] + 1
    return ip


def main():
    advent_ = "Advent21"
    bound, program = read_program(advent_)

    # Run program

    ip = 0

    x = Registers([0, 0, 0, 0, 0, 0])

    # while ip < len(program):
    #     if ip == 28:          # instruction 28 is the comparison with R0 so the first value of R4 that checks this
    #                           # comparison must be the first value that matches the code
    #         break
    #     ip = execute(bound, ip, program, x)
    # print("Part 1 - First value of R0 that will cause the program to stop after the least instructions", x.registers[4])

    prev = [x.registers[4]]
    ss = 0
    while ip < len(program):
        aa = ip+0
        ab = x.registers[:]
        ip = execute(bound, ip, program, x)
        if ip == 13: print(aa, program[ip], ab, x.registers)
        if ip == 28:
            prev.append(x.registers[4])
            if prev.count(prev[-1]) >= 3:
                print("Part 2 - Value of R0 that will cause the program to stop after the most instructions", prev[-2])
                print(prev)
                break
        ss += 1
        if ss == 100: break

    print("program has stopped", prev, x.registers)


if __name__ == "__main__":
    main()

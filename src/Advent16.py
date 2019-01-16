# Advent of Code 2018 Day 16
#
#
#

from AdventMachine import Registers

if __name__ == "__main__":

    file = open("../inputs/Advent16", 'r')

    # Extract inputs

    inputEOF = False
    input_phase = 1
    tests = []
    codes = []
    while not inputEOF:
        while input_phase == 1:
            try:
                before = next(file).rstrip("\n")
                if "Before" not in before:
                    next(file)
                    input_phase = 2
                    break
                before = list(map(int, before[9:19].split(", ")))
                code = list(map(int, next(file).rstrip("\n").split(" ")))
                after = list(map(int, next(file).rstrip("\n")[9:19].split(", ")))

                next(file)
                tests.append([before, code, after])
            except StopIteration:
                inputEOF = True
                input_phase = False
                break

        while input_phase == 2:
            try:
                codes.append(list(map(int, next(file).rstrip("\n").split(" "))))
            except StopIteration:
                inputEOF = True
                input_phase = False
                break

    # Part 1 - Run every command against every input to discover possible opcodes vs output
    commands = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr",
                "eqir", "eqri", "eqrr"]
    success = []
    success_count = []
    for reg, code, out in tests:

        opcode, inputA, inputB, outputC = code
        success_row = [opcode]
        for command in commands:
            x = Registers(reg)
            exec("x.{}(opcode, inputA, inputB, outputC)".format(command))
            success_row.append(out == x.registers)
        #       print(command, reg, code, x.registers, out == x.registers)
        success.append(success_row)
        success_count.append(sum(success_row))

    print("Part 1: Tests with three or more possible commands", len([x for x in success_count if x >= 3]))

    # Part 2a - Parse output grid from Part 1 to narrow down which command might be which

    opgrid = [[True for i in range(16)] for j in range(16)]
    for row in sorted(success):
        for x in range(16):
            if row[x + 1] == False:
                opgrid[row[0]][x] = False

    found_opcodes = [False for _ in range(16)]
    op_command = [None for _ in range(16)]
    while sum(found_opcodes) < 16:
        for row in range(len(opgrid)):
            rowsum = sum(opgrid[row])
            if rowsum == 1:
                opcode = opgrid[row].index(True)
                if not found_opcodes[opcode]:
                    found_opcodes[opcode] = True
                    for x in range(len(opgrid)):
                        if x != row:
                            opgrid[x][opcode] = False
                    op_command[row] = commands[opcode]
    for x in range(16):
        print("Part 2: Command", op_command[x], "now associated with opcode", x)

    # Part 2b - Calculate result

    x = Registers([0,0,0,0])
    for opcode, inputA, inputB, outputC in codes:
        exec("x.{}(opcode, inputA, inputB, outputC)".format(op_command[opcode]))
    print("Part 2: Final result after all commands run", x.registers)




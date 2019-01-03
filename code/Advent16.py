# Advent of Code 2018 Day 16

file = open("Advent16.txt", 'r')

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
            tests.append([code, before, after])
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

print(tests)
print(codes)
#
# Addition:
# addr (add register) stores into register C the result of adding register A and register B.
# addi (add immediate) stores into register C the result of adding register A and value B.
def addr(code, registers):

#
# Multiplication:
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
#
# Bitwise AND:
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
#
# Bitwise OR:
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
#
# Assignment:
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
# seti (set immediate) stores value A into register C. (Input B is ignored.)
#
# Greater-than testing:
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
#
# Equality testing:
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
#

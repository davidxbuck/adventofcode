# Advent of Code 2015
#
# From https://adventofcode.com/2016/day/5
#
import hashlib

inputs = 'uqwqemis'


# inputs = 'abc'

def find_hash(inputs, length):
    check = 0
    output = ''
    while True:
        hexdigest = hashlib.md5(bytes(inputs + str(check), encoding='utf8')).hexdigest()
        check += 1

        if hexdigest[:length] == '0' * length:
            output += hexdigest[length]
            print(output)
            if len(output) == 8:
                return output


def find_hash2(inputs, length):
    check = 0
    output = [' ' for _ in range(8)]
    while True:
        hexdigest = hashlib.md5(bytes(inputs + str(check), encoding='utf8')).hexdigest()
        check += 1

        if hexdigest[:length] == '0' * length:
            if '0' <= hexdigest[length] <= '7' and output[int(hexdigest[length])] == ' ':
                output[int(hexdigest[length])] = hexdigest[length + 1]
                print("".join(output))
            if ' ' not in output:
                return "".join(output)


print(f"AoC 2016 Day 5, Part 1 answer is {find_hash(inputs, 5)}")
print(f"AoC 2016 Day 5, Part 2 answer is {find_hash2(inputs, 5)}")

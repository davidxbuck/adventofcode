# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/4
#
import hashlib
inputs = 'ckczppom'
# inputs = 'abcdef'

def find_hash(inputs, length):
    check = 0
    while True:
        if hashlib.md5(bytes(inputs + str(check), encoding='utf8')).hexdigest()[:length] == '0' * length:
            return check
        check += 1
        if not check % 1000000:
            print(check)


print(f"AoC 2015 Day 4, Part 1 answer is {find_hash(inputs, 5)}")
print(f"AoC 2015 Day 4, Part 2 answer is {find_hash(inputs, 6)}")
# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/16

PUZZLE = "10111011111001111"


def solve(desired):
    data = PUZZLE
    while len(data) < desired:
        a = data
        b = "".join(str(1 - int(x)) for x in a)[::-1]
        data = a + "0" + b
    return data[:desired]


def checksum(check):
    while len(check) % 2 == 0:
        check = "".join(["1" if check[x] == check[x + 1] else "0" for x in range(0, len(check), 2)])
    return check


print(f"AoC 2016 Day 16 Part 1 answer is: {checksum(solve(272))}")
print(f"AoC 2016 Day 16 Part 2 answer is: {checksum(solve(35651584))}")

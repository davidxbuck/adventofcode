# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/21
import re

reg = r"""^(?:(swap position) (\d+) with position (\d+)|(swap letter) (\w) with letter (\w)|(rotate (?:right|left)) (\d+) steps?|(reverse) positions (\d+) through (\d)|(rotate based) on position of letter (\w)|(move) position (\d+) to position (\d+))$"""
cmds = [[x for x in re.findall(reg, row.strip())[0] if x] for row in open('../inputs/Advent2016_21.txt', 'r')]


def forwards(inp):
    inp = list(inp)
    for command in cmds:
        cmd = command[0]

        if cmd == "swap position":
            x, y = map(int, command[1:])
            inp[x], inp[y] = inp[y], inp[x]
        elif cmd == "swap letter":
            x, y = inp.index(command[1]), inp.index(command[2])
            inp[x], inp[y] = inp[y], inp[x]
        elif cmd == "reverse":
            x, y = sorted(map(int, command[1:]))
            if x == 0:
                inp = inp[:x] + inp[y::-1] + inp[y + 1:]
            else:
                inp = inp[:x] + inp[y:x - 1:-1] + inp[y + 1:]
        elif cmd == "move":
            x, y = map(int, command[1:])
            inp[y:y] = inp.pop(x)
        elif cmd == "rotate right":
            x = int(command[1])
            inp = inp[len(inp) - x:] + inp[:len(inp) - x]
        elif cmd == "rotate left":
            x = int(command[1])
            inp = inp[x:] + inp[:x]
        elif cmd == "rotate based":
            x = 1 + inp.index(command[1])
            if x >= 5:
                x += 1
            inp = inp[len(inp) - x:] + inp[:len(inp) - x]
        else:
            print("Error", cmd)
    return "".join(inp)


def backwards(inp):
    inp = list(inp)
    for command in cmds[::-1]:
        cmd = command[0]

        if cmd == "swap position":
            x, y = map(int, command[1:])
            inp[x], inp[y] = inp[y], inp[x]
        elif cmd == "swap letter":
            x, y = inp.index(command[1]), inp.index(command[2])
            inp[x], inp[y] = inp[y], inp[x]
        elif cmd == "reverse":
            x, y = sorted(map(int, command[1:]))
            if x == 0:
                inp = inp[:x] + inp[y::-1] + inp[y + 1:]
            else:
                inp = inp[:x] + inp[y:x - 1:-1] + inp[y + 1:]
        elif cmd == "move":
            x, y = map(int, command[1:])
            inp[x:x] = inp.pop(y)
        elif cmd == "rotate right":
            x = int(command[1])
            inp = inp[x:] + inp[:x]
        elif cmd == "rotate left":
            x = int(command[1])
            inp = inp[len(inp) - x:] + inp[:len(inp) - x]
        elif cmd == "rotate based":
            test = inp
            for y in range(len(inp)):
                test = test[1:] + test[:1]
                x = 1 + test.index(command[1])
                if x >= 5:
                    x += 1
                test2 = test[len(test) - x:] + test[:len(test) - x]
                if test2 == inp:
                    inp = test
                    break
        else:
            print("Error", cmd)
    return "".join(inp)


def main():
    part1 = 'abcdefgh'
    print(f"AoC 2016 Day 21, Part 1 answer is {forwards(part1)}")
    part2 = 'fbgdceah'
    result = backwards(part2)
    if forwards(result) == part2:
        print(f"AoC 2016 Day 21, Part 2 answer is {result}")


if __name__ == '__main__':
    main()

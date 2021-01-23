# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/7
#

import re


def importer():
    inputs = [data.strip() for data in open('../inputs/Advent2015_07.txt', 'r')]
    return [re.findall(r"^([a-z0-9]*)\s*(NOT|OR|AND|RSHIFT|LSHIFT)*\s*([a-z0-9]*) -> ([a-z]{1,2})$", entry)[0] for entry
            in inputs]


def cleanup(cmds, to_delete):
    for cmd in sorted(to_delete, reverse=True):
        cmds.pop(cmd)
    return cmds


def int_or_val(x, wires):
    if x.isdigit():
        x = int(x)
    else:
        x = wires[x]
    return x


commands = importer()


def find_a(cmds, override=-1):
    wires = {}
    while 'a' not in wires:
        to_del = []
        for ix, cmd in enumerate(cmds):
            a, b, c, d = cmd
            if a.isdigit() and not b and not c:
                if d == 'b' and override > 1:
                    wires[d] = override
                else:
                    wires[d] = int(a)
                to_del.append(ix)
            elif not a and b == "NOT" and c.isdigit():
                wires[d] = int(c) ^ 0xFFFF
                to_del.append(ix)
            elif (a.isdigit() or a in wires) and (c.isdigit() or c in wires):
                a = int_or_val(a, wires)
                c = int_or_val(c, wires)
                if b == "OR":
                    wires[d] = a | c
                elif b == "AND":
                    wires[d] = a & c
                elif b == "RSHIFT":
                    wires[d] = a >> c
                elif b == "LSHIFT":
                    wires[d] = (a << c) & 0xFFFF
                to_del.append(ix)
            elif b == "NOT" and c in wires:
                wires[d] = wires[c] ^ 0xFFFF
                to_del.append(ix)
            elif a in wires and not b and not c:
                wires[d] = wires[a]
                to_del.append(ix)
        cmds = cleanup(cmds, to_del)
    return wires['a']


wire_a = find_a(commands.copy())
print(f"AoC 2015 Day 7, Part 1 answer is {wire_a}")
print(f"AoC 2015 Day 7, Part 2 answer is {find_a(commands.copy(), wire_a)}")

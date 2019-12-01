# Advent of Code 2018 Day 20

# Read file and extract tree

from collections import defaultdict

file = open("../inputs/Advent20", 'r')
inp = file.read().strip()[1:-1]

def getitem(s, depth=0):
    out = [""]
    while s:
        c = s[0]
        if depth and (c == '|' or c == ')'):
            return out, s
        if c == '(':
            x = getgroup(s[1:], depth + 1)
            if x:
                out = [a + b for a in out for b in x[0]]
                s = x[1]
                continue
        if c == '\\' and len(s) > 1:
            s = s[1:]
            c = c + s[1]

        out = [a + c for a in out]
        s =  s[1:]

    return out, s


def getgroup(s, depth):
    print("Current depth", depth)
    out = []
    pipe = False
    while s:
        g, s = getitem(s, depth)
        if not s: break
        out += g

        if s[0] == ')':
            if pipe: return out, s[1:]
            return ['(' + a + ')' for a in out], s[1:]

        if s[0] == '|':
            pipe = True
            s = s[1:]

    return None
s = inp
print(s)
print(getitem(s))
for item in getitem(s)[0]:
    print(item)

print("Program terminated")
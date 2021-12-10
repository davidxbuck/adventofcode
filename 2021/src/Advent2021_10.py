# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/10
#

SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
AC_SCORES = {'(': 1, '[': 2, '{': 3, '<': 4}
PAIRS = {')': '(', ']': '[', '}': '{', '>': '<'}

lines = [row.strip() for row in open("../inputs/Advent2021_10.txt", "r")]

errors = []
auto_complete = []

for ix, line in enumerate(lines):
    stack = []
    incorrect = False
    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            prev = stack.pop()
            if PAIRS[char] != prev:
                errors.append(char)
                incorrect = True
                break
    if not incorrect:
        total = 0
        for char in stack[::-1]:
            total = total * 5 + AC_SCORES[char]
        auto_complete.append(total)

print(f'Day 10, Part 1 {sum(SCORES[error] for error in errors)}')
print(f'Day 10, Part 2 {sorted(auto_complete)[(len(auto_complete) - 1) // 2]}')

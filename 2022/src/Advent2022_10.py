# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/10
#

moves = [x.split(' ') for x in open(f'../inputs/day10.txt', 'r').read().split('\n')]

clock = {}
step = 0
current = 1

for x in moves:
    step += 1
    clock[step] = {}
    clock[step]['command'] = x[0]
    if x[0] == 'noop':
        clock[step]['x_during'] = current
        clock[step]['x_after'] = current
        clock[step]['score'] = current * step
        clock[step]['increment'] = 0
    elif x[0] == 'addx':
        clock[step]['increment'] = 0
        clock[step]['x_during'] = current
        clock[step]['x_after'] = current
        clock[step]['score'] = current * step
        step += 1
        clock[step] = {}
        clock[step]['command'] = x[0]
        clock[step]['increment'] = x[1]
        clock[step]['x_during'] = current
        clock[step]['score'] = current * step
        current += int(x[1])
        clock[step]['x_after'] = current

print(f'Day 10, Part 1 {sum(clock[x]["score"] for x in list(range(20, 222, 40)))}')

crt = []
row = -1
for x in range(1, 241):
    pos = x % 40 - 1
    if pos == 0:
        row += 1
        crt.append([])
    if clock[x]['x_during'] - 1 <= pos <= clock[x]['x_during'] + 1:
        crt[row].append('#')
    else:
        crt[row].append('.')

output = "\n".join("".join(x) for x in crt)
print(f'Day 10, Part 2 \n{output}')

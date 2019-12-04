# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/3
#
from itertools import count, islice

import numpy as np

with open('../inputs2019/Advent2019_03.txt', 'r') as f:
    inputs = [line.strip().split(',') for line in f]
# Trial inputs
#
# inputs = [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
#            ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
#
# inputs = [['R8','U5','L5','D3'],
#           ['U7','R6','D4','L4']]
#
# inputs = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
#           ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]
#

# Rather than guess an enormous grid size, evaluate the max size from the inputs

rightmax = leftmax = upmax = downmax = 0

for line in inputs:
    x = y = 0
    for move in line:
        left, up, right, down = (move[0] == 'L', move[0] == 'U', move[0] == 'R', move[0] == 'D')
        distance = int(move[1:])
        if left:
            x -= int(distance)
            leftmax = min(x, leftmax)
        elif up:
            y += int(distance)
            upmax = max(y, upmax)
        elif right:
            x += int(distance)
            rightmax = max(x, rightmax)
        elif down:
            y -= int(distance)
            downmax = min(y, downmax)

# Rebase grid at 0,0 and set central_port
x_width = rightmax - leftmax + 1
y_height = upmax - downmax + 1
central_port = [-leftmax, -downmax]



# Map each circuit and combine to find intersections
intergrid = np.zeros([x_width, y_height], dtype=int)
for line in inputs:
    x, y = central_port
    grid = np.zeros([x_width, y_height], dtype=int)
    for move in line:
        left, up, right, down = (move[0] == 'L', move[0] == 'U', move[0] == 'R', move[0] == 'D')
        distance = int(move[1:])
        if left:
            grid[x - distance:x, y] = 1
            x -= int(distance)
        elif up:
            grid[x:x + 1, y + 1:y + distance + 1] = 1
            y += int(distance)
        elif right:
            grid[x + 1:x + distance + 1, y] = 1
            x += int(distance)
        elif down:
            grid[x, y - distance:y] = 1
            y -= int(distance)
    intergrid += grid

# Determine coordinates of intersections and Manhattan Distances from control point

intersections = np.where(intergrid > 1)
intersections = list(zip(*intersections))
distances = [abs(x - central_port[0]) + abs(y - central_port[1]) for x, y in intersections]

print(f'AoC 2019 Day 2, Part 1 Nearest intersection is: {intersections[distances.index(min(distances))]} at a distance of {min(distances)}')

# Repeat mapping of both circuits but capture the number of total number of moves for each datapoint

grid = np.zeros([x_width, y_height], dtype=int)
for line in inputs:
    x, y = central_port
    counter = count(1)
    for move in line:
        left, up, right, down = (move[0] == 'L', move[0] == 'U', move[0] == 'R', move[0] == 'D')
        distance = int(move[1:])
        if left:
            grid[x - distance:x, y] += list(islice(counter, distance))
            x -= int(distance)
        elif up:
            grid[x:x + 1, y + 1:y + distance + 1] += list(islice(counter, distance))
            y += int(distance)
        elif right:
            grid[x + 1:x + distance + 1, y] += list(islice(counter, distance))
            x += int(distance)
        elif down:
            grid[x, y - distance:y] += list(islice(counter, distance))
            y -= int(distance)

# Determine the min of the number of moves for each of the known interestions

moves = [grid[x, y] for x, y in intersections]

print(f'AoC 2019 Day 2, Part 2 Nearest intersection is: {min(moves)} steps ')

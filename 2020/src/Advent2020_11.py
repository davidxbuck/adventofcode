# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/11
#
import numpy as np

seats = np.array(list(list(row.strip()) for row in open('../inputs/Advent2020_11.txt', 'r')))
padded = np.array(seats.shape) + [2, 2]
padded_seats = np.empty(padded, dtype=str)
padded_seats[1:padded[0] - 1, 1:padded[1] - 1] = seats.copy()
next_seats = np.empty_like(padded_seats, dtype=str)
prev_seats = np.empty_like(padded_seats, dtype=str)
x_to, y_to = np.array(seats.shape) + 1

while not (padded_seats == prev_seats).all():
    prev_seats = padded_seats.copy()
    for x in range(1, x_to):
        for y in range(1, y_to):
            if padded_seats[x, y] in ['#', 'L']:
                occupied = np.count_nonzero(padded_seats[x - 1:x + 2, y - 1:y + 2] == '#') - int(
                    padded_seats[x, y] == '#')
                if occupied == 0:
                    next_seats[x, y] = '#'
                elif occupied >= 4:
                    next_seats[x, y] = 'L'
                else:
                    next_seats[x, y] = padded_seats[x, y]
    padded_seats = next_seats.copy()

print(np.count_nonzero(padded_seats == '#'))

padded = np.array(seats.shape) + [2, 2]
padded_seats = np.empty(padded, dtype=str)
padded_seats[1:padded[0] - 1, 1:padded[1] - 1] = seats.copy()
next_seats = np.empty_like(padded_seats, dtype=str)
prev_seats = np.empty_like(padded_seats, dtype=str)
x_to, y_to = np.array(seats.shape) + 1

NW = [[-1 * x, 1 * x] for x in range(1, max(seats.shape))]
N = [[0, 1 * x] for x in range(1, max(seats.shape))]
NE = [[1 * x, 1 * x] for x in range(1, max(seats.shape))]
E = [[1 * x, 0] for x in range(1, max(seats.shape))]
SE = [[1 * x, -1 * x] for x in range(1, max(seats.shape))]
S = [[0, -1 * x] for x in range(1, max(seats.shape))]
SW = [[-1 * x, -1 * x] for x in range(1, max(seats.shape))]
W = [[-1 * x, 0] for x in range(1, max(seats.shape))]
angles = [NW, N, NE, E, SE, S, SW, W]

while not (padded_seats == prev_seats).all():
    prev_seats = padded_seats.copy()
    for x in range(1, x_to):
        for y in range(1, y_to):
            if padded_seats[x, y] in ['#', 'L']:
                occupied = 0
                for angle in angles:
                    for ang_x, ang_y in angle:
                        if 1 <= x + ang_x <= x_to and 1 <= y + ang_y <= y_to:
                            if padded_seats[x + ang_x, y + ang_y] in ['#', 'L']:
                                occupied += int(padded_seats[x + ang_x, y + ang_y] == '#')
                                break
                        else:
                            break
                if occupied == 0:
                    next_seats[x, y] = '#'
                elif occupied >= 5:
                    next_seats[x, y] = 'L'
                else:
                    next_seats[x, y] = padded_seats[x, y]
    padded_seats = next_seats.copy()

print(np.count_nonzero(padded_seats == '#'))

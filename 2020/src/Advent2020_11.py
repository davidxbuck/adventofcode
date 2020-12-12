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

print(f"""AoC 2020 Day 11 Part 1 answer is: {np.count_nonzero(padded_seats == '#')}""")

padded_seats[1:padded[0] - 1, 1:padded[1] - 1] = seats.copy()
next_seats = np.empty_like(padded_seats, dtype=str)
prev_seats = np.empty_like(padded_seats, dtype=str)

directions = [(-1, 1), (0, 1), (1, 1), (1, 0,), (1, -1), (0, -1), (-1, -1), (-1, 0)]

while not (padded_seats == prev_seats).all():
    prev_seats = padded_seats.copy()
    for x in range(1, x_to):
        for y in range(1, y_to):
            if padded_seats[x, y] in ['#', 'L']:
                occupied = 0
                for ang_x, ang_y in directions:
                    dist = 0
                    while True:
                        dist += 1
                        x_check = x + ang_x * dist
                        y_check = y + ang_y * dist
                        if 1 <= x_check <= x_to and 1 <= y_check <= y_to:
                            if padded_seats[x_check, y_check] in ['#', 'L']:
                                occupied += int(padded_seats[x_check, y_check] == '#')
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

print(f"""AoC 2020 Day 11 Part 2 answer is: {np.count_nonzero(padded_seats == '#')}""")

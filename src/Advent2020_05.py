# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/5
#

def get_seats(filename=''):
    inputs = (row.strip() for row in open(f'../inputs2020/Advent2020_05{filename}.txt', 'r'))
    return set(map(lambda x: int(x.translate(str.maketrans("FBRL", "0110")), 2), inputs))


def find_seat(occupied_seats):
    for possibility in set(range(min(occupied_seats), max(occupied_seats))).difference(occupied_seats):
        if possibility - 1 in occupied_seats and possibility + 1 in occupied_seats:
            return possibility


seats = get_seats()
print(f"""AoC 2020 Day 5 Part 1 answer is: {max(seats)}""")
print(f"""AoC 2020 Day 5 Part 2 answer is: {find_seat(seats)}""")

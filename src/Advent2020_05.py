# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/5
#

def get_seats(filename=''):
    inputs = (row for row in open(f'../inputs2020/Advent2020_05{filename}.txt', 'r'))
    seats = map(lambda x: x.translate(str.maketrans("FBRL", "0110")), inputs)
    return list(map(lambda x: int(x[:7], 2) * 8 + int(x[7:], 2), seats))


def find_seat(occupied_seats):
    empty_seats = set(range(128 * 8)).difference(occupied_seat_set := set(occupied_seats))
    for possibility in empty_seats:
        if possibility - 1 in occupied_seat_set and possibility + 1 in occupied_seat_set:
            return possibility


seats = get_seats()
print(f"""AoC 2020 Day 5 Part 1 answer is: {max(seats)}""")
print(f"""AoC 2020 Day 5 Part 2 answer is: {find_seat(seats)}""")

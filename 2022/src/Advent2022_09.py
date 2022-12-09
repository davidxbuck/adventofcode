# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/9
#

moves = [x.split(' ') for x in open(f'../inputs/day9.txt', 'r').read().split('\n')]
moves = [[x, int(y)] for x, y in moves]


def move_tail(no_knots):
    knots = {x: 0j for x in range(no_knots)}
    tail_seen = {0j}
    moving = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

    for move, count in moves:
        for step in range(count):
            knots[0] += moving[move]
            for knot in range(1, no_knots):
                if abs(knots[knot].real - knots[knot - 1].real) < 2 and abs(
                        knots[knot].imag - knots[knot - 1].imag) < 2:
                    continue
                if knots[knot].real == knots[knot - 1].real:
                    if knots[knot].imag < knots[knot - 1].imag:
                        knots[knot] += 1j
                    else:
                        knots[knot] -= 1j
                elif knots[knot].imag == knots[knot - 1].imag:
                    if knots[knot].real < knots[knot - 1].real:
                        knots[knot] += 1
                    else:
                        knots[knot] -= 1
                else:
                    if abs(knots[knot].real - knots[knot - 1].real) == 2 and abs(
                            knots[knot].imag - knots[knot - 1].imag) == 2:
                        knots[knot] = (knots[knot].real + (knots[knot - 1].real - knots[knot].real) // 2) + (
                                    knots[knot].imag + (knots[knot - 1].imag - knots[knot].imag) // 2) * 1j
                    elif abs(knots[knot].real - knots[knot - 1].real) == 2:
                        knots[knot] = (knots[knot].real + (knots[knot - 1].real - knots[knot].real) // 2) + knots[
                            knot - 1].imag * 1j
                    else:
                        knots[knot] = (knots[knot].imag + (knots[knot - 1].imag - knots[knot].imag) // 2) * 1j + knots[
                            knot - 1].real
            tail_seen.add(knots[no_knots - 1])
    return len(tail_seen)


print(f'Day 9, Part 1 {move_tail(2)}')
print(f'Day 9, Part 2 {move_tail(10)}')

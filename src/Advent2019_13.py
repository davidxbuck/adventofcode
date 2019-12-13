# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/13
#

from Advent2019_Intcode import Intcode


def main():
    inputs = list(map(int, [code.strip().split(',') for code in open('../inputs2019/Advent2019_13.txt', 'r')][0]))

    terminated = False
    game = Intcode(inputs[:], mode='run')
    count = 0
    while not terminated:
        game.run()
        game.run()
        draw, terminated = game.run()
        if draw == 2:
            count += 1
    print(f'AoC 2019 Day 12, Part 1: Number of blocks is {count}')

    terminated = False
    game = Intcode(inputs[:], inp=[0], mode='run')
    game.program[0] = 2  # Insert 2 quarters
    paddle = False
    while not terminated:
        draw_x, terminated = game.run()
        draw_y, terminated = game.run()
        draw, terminated = game.run()
        if draw_x == -1 and draw_y == 0:
            current_score = draw
            continue
        if draw == 3:
            paddle = draw_x
        if draw == 4:
            ball = draw_x
            if paddle:
                if paddle < ball:
                    game.next_inp(1)
                elif paddle > ball:
                    game.next_inp(-1)
                else:
                    game.next_inp(0)

    print(f'AoC 2019 Day 12, Part 2: High Score {current_score}')


if __name__ == '__main__':
    grid = main()

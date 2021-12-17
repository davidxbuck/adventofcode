# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/17
#
import re

min_x, max_x, min_y, max_y = list(map(int, [
    re.findall(r"^target area: x=(-\d+|\d+)..(-\d+|\d+), y=(-\d+|\d+)..(-\d+|\d+)$", entry.strip())[0] for entry in
    open('../inputs/Advent2021_17.txt', 'r')][0]))


def check_target(x, y):
    if x > max_x or y < min_y:
        return 'beyond'
    elif min_x <= x <= max_x and min_y <= y <= max_y:
        return 'within'


max_height = 0
max_velocity = None
count = 0

for velocity_x in range(1, max_x * 2):
    for vel_y in range(-max_x, max_x * 2):
        vel_x = velocity_x
        velocity = (vel_x, vel_y)
        max_loop_y = y = x = 0
        while True:
            x += vel_x
            if vel_x > 0:
                vel_x -= 1
            elif vel_x < 0:
                vel_x += 1
            y += vel_y
            vel_y -= 1
            max_loop_y = max(max_loop_y, y)
            check = check_target(x, y)
            if check == 'beyond':
                break
            elif check == 'within':
                count += 1
                if max_loop_y > max_height:
                    max_height = max_loop_y
                    max_velocity = velocity
                break

print(f'Day 17, Part 1: {max_height}')
print(f'Day 17, Part 1: {count}')

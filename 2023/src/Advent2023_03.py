# Advent of Code 2023
#
# From https://adventofcode.com/2023/day/3
#



import numpy as np

data = np.array([list(x) for x in open('../inputs/day3.txt', 'r').read().split('\n')])
max_y, max_x = data.shape
grid = np.full((max_y + 2, max_x + 2), '.')
grid[1:max_y + 1, 1:max_x + 1] = data.copy()
all_numbers = []
for y in range(1, max_y + 1):
    x = 1
    while x < max_x + 1:
        digits = ''
        if not grid[y, x].isdigit():
            x += 1
            continue
        else:
            x_start = x
            digits = grid[y, x]
            x += 1
            while grid[y, x].isdigit():
                digits += grid[y, x]
                x += 1
            sub_grid = grid[y-1:y+2, x_start-1:x+1]
            has_symbol = len([z for z in "".join(sub_grid.flatten().tolist()).replace('.','') if not z.isdigit()]) > 0
            if has_symbol:
                all_numbers.append(int(digits))

print(f'Day 3, Part 1 {sum(all_numbers)}')


def above_or_below(above=True):
    numbers = []
    displacement = -1 if above else 1
    above = grid[y + displacement, x]
    above_left = grid[y + displacement, x - 1]
    above_left2 = grid[y + displacement, x - 2]
    above_left3 = grid[y + displacement, x - 3]
    above_right = grid[y + displacement, x + 1]
    above_right2 = grid[y + displacement, x + 2]
    above_right3 = grid[y + displacement, x + 3]
    if above.isdigit():
        digits = above
        if above_left.isdigit():
            digits = above_left + digits
            if above_left2.isdigit():
                digits = above_left2 + digits
            elif above_right.isdigit():
                digits = digits + above_right
        elif above_right.isdigit():
            digits += above_right
            if above_right2.isdigit():
                digits += above_right2
        numbers.append(int(digits))
    else:
        if above_right.isdigit():
            digits = above_right
            if above_right2.isdigit():
                digits += above_right2
                if above_right3.isdigit():
                    digits += above_right3
            numbers.append(int(digits))
        if above_left.isdigit():
            digits = above_left
            if above_left2.isdigit():
                digits = above_left2 + digits
                if above_left3.isdigit():
                    digits = above_left3 + digits
            numbers.append(int(digits))
    return numbers

check = []
results = []
for y in range(1, max_y + 1):
    x = 1
    numbers = None
    while x < max_x + 1:
        if grid[y, x] != '*':
            x += 1
            continue
        numbers = []
        numbers += above_or_below(above=True)
        numbers += above_or_below(above=False)
        left_digits = ''
        for left_x in range(x - 1, x - 4, -1):
            if grid[y, left_x].isdigit():
                left_digits = grid[y, left_x] + left_digits
            else:
                break
        if left_digits:
            numbers.append(int(left_digits))
        right_digits = ''
        for right_x in range(x + 1, x + 4, 1):
            if grid[y, right_x].isdigit():
                right_digits += grid[y, right_x]
            else:
                break
        if right_digits:
            numbers.append(int(right_digits))
        if len(numbers) == 2:
            result = numbers[0] * numbers[1]
            results.append(result)
            check.append(((y, x), numbers, result))
        x += 1


        

print(f'Day 3, Part 2 {sum(results)}')

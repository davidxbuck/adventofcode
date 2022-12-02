#
# From https://adventofcode.com/2022/day/2
#

data = [row.strip().split(' ') for row in open('../inputs/day2.txt', 'r')]

choice = {'X': 1, 'Y': 2, 'Z': 3}
game = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0, ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6, ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,}

print(f'Day 2, Part 1 {sum(game[(x, y)] + choice[y] for x, y in data)}')
choice2 = {'X': 0, 'Y': 3, 'Z': 6}
game2 = {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2, ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3, ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1, }

print(f'Day 2, Part 2 {sum(game2[(x, y)] + choice2[y] for x, y in data)}')

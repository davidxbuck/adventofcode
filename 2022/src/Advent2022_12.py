# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/12
#
import numpy as np
from queue import PriorityQueue


def manhattan_distance(a, b):
    return np.abs(np.array(a) - np.array(b)).sum()


def find_path(grid, start_position=None):
    grid = grid.copy()
    start = ord('S') - 97
    end = ord('E') - 97
    if not start_position:
        start_pos = np.where(grid == start)
        x = start_pos[0][0]
        y = start_pos[1][0]
        grid[x, y] = 0
    else:
        x, y = start_position
    end_pos = np.where(grid == end)
    end_x = end_pos[0][0]
    end_y = end_pos[1][0]
    grid[end_x, end_y] = 25
    end_pos = (end_x, end_y)
    max_x, max_y = grid.shape
    max_x -= 1
    max_y -= 1
    q = PriorityQueue()
    q.put((0, x, y))
    visited = {(x, y): []}
    while not q.empty():
        _, x, y = q.get()
        height = grid[x, y]
        possible = []
        if 0 <= x - 1 and grid[x - 1, y] <= height + 1:
            possible.append((x - 1, y))
        if 0 <= y - 1 and grid[x, y - 1] <= height + 1:
            possible.append((x, y - 1))
        if x + 1 <= max_x and grid[x + 1, y] <= height + 1:
            possible.append((x + 1, y))
        if y + 1 <= max_y and grid[x, y + 1] <= height + 1:
            possible.append((x, y + 1))
        best_path = visited[(x, y)]
        for next_try in possible:
            test_path = best_path.copy()
            test_path.append(next_try)
            if not (next_try in visited) or len(visited[next_try]) > len(test_path):
                visited[next_try] = test_path
                q.put((manhattan_distance(next_try, end_pos), *next_try))
    return len(visited[end_pos]) if end_pos in visited else 99999


grid = np.loadtxt('../inputs/day12.txt', dtype=str)
grid = np.array([list(map(ord, list(x))) for x in grid]) - 97

print(f'Day 12, Part 1 {find_path(grid)}')

shortest = 99999
for start in zip(*np.where(grid == 0)):
    test = find_path(grid, start_position=start)
    shortest = min(shortest, test)
    # definitely some serious optimisation could be done here
print(f'Day 12, Part 2 {shortest}')

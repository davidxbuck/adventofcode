# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/20
#


from collections import Counter
from collections import defaultdict
from math import prod

import numpy as np


class Tile:
    def __init__(self, data):
        self.tile = np.array(list(list(row) for row in data[1:11]))
        self.id = int(data[0].strip("Tile: "))
        self.extract_edges()

    def extract_edges(self):
        self.edges = np.array(("".join(self.tile[:, 0].tolist()[::-1]), "".join(self.tile[0, :].tolist()),
                               "".join(self.tile[-1, :].tolist()[::-1]), "".join(self.tile[:, -1].tolist())))
        for edge in self.edges:
            edge_dict[edge].add(self.id)
            edge_dict[edge[::-1]].add(self.id)

    @property
    def left_edge(self):
        return "".join(self.tile[:, 0].tolist()[::-1])

    @property
    def right_edge(self):
        return "".join(self.tile[:, -1].tolist())

    @property
    def top_edge(self):
        return "".join(self.tile[0, :].tolist())

    @property
    def bottom_edge(self):
        return "".join(self.tile[-1, :].tolist()[::-1])

    def rotate(self):
        self.tile = np.rot90(self.tile)

    def flip(self):
        for edge in self.edges:
            edge_dict[edge].pop(edge_dict[edge].index(edge))
        self.tile = np.fliplr(self.tile)
        self.extract_edges()

    def orient(self, edge, where):
        edge = edge[::-1]
        for x in range(2):
            for _ in range(4):
                if where == "top" and self.top_edge == edge:
                    return
                if where == "left" and self.left_edge == edge:
                    return
                self.tile = np.rot90(self.tile)
            self.tile = np.fliplr(self.tile)
        print("Not found error")


class Grid:
    def __init__(self, corner, tile_dict):
        self.grid = np.empty((12, 12), dtype=object)
        self.grid[0, 0] = tile_dict[corner]
        # Top left corner
        while self.grid[0, 0].left_edge not in sides or self.grid[0, 0].top_edge not in sides:
            self.grid[0, 0].rotate()
        # Top row
        for y in range(1, 12):
            edge_to_match = self.grid[0, y - 1].right_edge
            tile_to_use = list(edge_dict[edge_to_match] - {self.grid[0, y - 1].id})[0]
            self.grid[0, y] = tile_dict[tile_to_use]
            self.grid[0, y].orient(edge_to_match, "left")
        # Remainder
        for x in range(1, 12):
            for y in range(0, 12):
                edge_to_match = self.grid[x - 1, y].bottom_edge
                tile_to_use = list(edge_dict[edge_to_match] - {self.grid[x - 1, y].id})[0]
                self.grid[x, y] = tile_dict[tile_to_use]
                self.grid[x, y].orient(edge_to_match, "top")


class Map:
    def __init__(self, grid):
        self.grid = grid.grid
        self.merged = np.empty((96, 96), dtype=object)
        self.x, self.y = self.merged.shape
        for x in range(0, 12):
            for y in range(0, 12):
                self.merged[x * 8: (x + 1) * 8, y * 8: (y + 1) * 8] = self.grid[x, y].tile[1:9, 1:9]
        self.monster = Monster()

    def print_map(self):
        print(" ", end="")
        for x in range(96):
            print(x % 8, end="")
        print()
        for x in range(96):
            print(x % 8, end="")
            print("".join(self.count_grid[x, :].tolist()).replace('.', ' '), end="")
            print(x % 8)
        print(" ", end="")
        for x in range(96):
            print(x % 8, end="")
        print()

    def search_map(self):
        print(f"\nSearching this way:\n{self.monster}\n")
        return_value = False
        for x in range(0, self.x - self.monster.x):
            for y in range(0, self.y - self.monster.y):
                compare = self.merged[x: x + self.monster.x, y: y + self.monster.y]
                if all(compare[cx, cy] == "#" for cx, cy in self.monster.indexes):
                    for cx, cy in self.monster.indexes:
                        self.count_grid[x + cx, y + cy] = 'O'
                    return_value = True
        return return_value

    def search_all_maps(self):
        self.count_grid = self.merged.copy()
        for _ in range(2):
            for _ in range(4):
                if self.search_map():
                    self.monster.flip()
                    self.search_map()
                    return
                self.merged = np.rot90(self.merged)
            self.merged = np.fliplr(self.merged)
        print("Not found error")


class Monster:
    def __init__(self):
        self.monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
        self.monster = np.array(list(list(row) for row in self.monster.split('\n')))
        self.monster = np.fliplr(self.monster)
        self.indexes = np.argwhere(self.monster == '#')
        self.x, self.y = self.monster.shape

    def flip(self):
        self.monster = np.fliplr(self.monster)
        self.indexes = np.argwhere(self.monster == '#')

    def __str__(self):
        nessy = "\n".join(["".join(row.tolist()) for row in self.monster])
        return nessy


# Extract inputs
filename = ''
data = [x.split('\n') for x in open(f'../inputs/Advent2020_20{filename}.txt', 'r').read().split('\n\n')]

edge_dict = defaultdict(set)

tiles = [Tile(tile) for tile in data]
tile_dict = {tile.id: tile for tile in tiles}

# From matched edges, anything without a match is a side
sides = {k: v for k, v in edge_dict.items() if len(v) == 1}

# Extract IDs of sides and count number of matched edges. If only four matches, it's a corner
side_pieces = [list(v)[0] for v in sides.values()]
side_count = Counter(side_pieces)
corners = [side for side, v in side_count.items() if v == 4]

print(f"""AoC 2020 Day 20 Part 1 answer is: {prod(corners)}""")

grid = Grid(corners[0], tile_dict)
monster_map = Map(grid)

monster_map.search_all_maps()
monster_map.print_map()
print(f"""AoC 2020 Day 20 Part 1 answer is: {sum(sum(monster_map.count_grid == "#"))}""")

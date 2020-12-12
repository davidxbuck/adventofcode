# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/12
#
from collections import deque


class Position:
    def __init__(self):
        self.compass = {"E": 1, "S": -1j, "W": -1, "N": +1j}
        self.rotation = {"L": 1, "R": -1}
        self.waypoint_rotation = {"R": [1, -1j, -1, 1j], "L": [1, 1j, -1, -1j]}
        self.facing = deque(self.compass.values())
        self.position = 0
        self.instructions = self.action = self.quantity = None
        self.waypoint = 10 + 1j

    def get_instructions(self, filename=""):
        self.instructions = \
            [[(x := row.strip())[0], int(x[1:])] for row in open(f'../inputs/Advent2020_12{filename}.txt', 'r')]

    def move(self, movement):
        self.action, self.quantity = movement
        if self.action in self.compass:
            self.position += self.compass[self.action] * self.quantity
        elif self.action in self.rotation:
            self.facing.rotate(self.rotation[self.action] * self.quantity // 90)
        elif self.action == "F":
            self.position += self.facing[0] * self.quantity

    def waypoint_move(self, movement):
        self.action, self.quantity = movement
        if self.action in self.compass:
            self.waypoint += self.compass[self.action] * self.quantity
        elif self.action in self.rotation:
            self.waypoint *= self.waypoint_rotation[self.action][self.quantity // 90]
        elif self.action == "F":
            self.position += self.waypoint * self.quantity

    def part1(self):
        self.position = 0
        for movement in self.instructions:
            self.move(movement)
        return int(abs(self.position.imag) + abs(self.position.real))

    def part2(self):
        self.position = 0
        for movement in self.instructions:
            self.waypoint_move(movement)
        return int(abs(self.position.imag) + abs(self.position.real))


def main():
    pos = Position()
    pos.get_instructions(filename="")
    print(f"""AoC 2020 Day 12 Part 1 answer is: {pos.part1()}""")
    print(f"""AoC 2020 Day 12 Part 2 answer is: {pos.part2()}""")


if __name__ == '__main__':
    main()

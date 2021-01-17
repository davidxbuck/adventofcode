# Advent of Code 2015
#
# From https://adventofcode.com/2015/day/14

import re


class Deer:
    def __init__(self, filename=''):
        self.data = [re.findall(r'^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$',
                                row.strip())[0] for row in open(f'../inputs/Advent2015_14{filename}.txt', 'r')]
        self.deer = {}

    def reset(self):
        self.deer = {x[0]: {"speed": int(x[1]), "fly": int(x[2]), "rest": int(x[3]), "points": 0} for x in self.data}
        self.all_deer = {k for k in self.deer.keys()}

    def distance(self, name, time):
        period = self.deer[name]["fly"] + self.deer[name]["rest"]
        periods = time // period
        part_period = time % period
        if part_period > self.deer[name]["fly"]:
            periods += 1
        else:
            periods += part_period / self.deer[name]["fly"]
        self.deer[name]["distance"] = int(periods * self.deer[name]["speed"] * self.deer[name]["fly"])
        return periods * self.deer[name]["speed"] * self.deer[name]["fly"]

    def points(self):
        max_dist = max(v["distance"] for v in self.deer.values())
        for reindeer in self.deer.values():
            if reindeer["distance"] == max_dist:
                reindeer["points"] += 1


filename = ""
time = 2503
deer = Deer(filename)
deer.reset()

print(f"AoC 2015 Day 14, Part 1 answer is {max(deer.distance(reindeer, time) for reindeer in deer.all_deer)} km")

deer.reset()
for x in range(1, time + 1):
    for y in deer.all_deer:
        deer.distance(y, x)
    deer.points()
print(f"AoC 2015 Day 14, Part 2 answer is {max(z['points'] for z in deer.deer.values())} points")

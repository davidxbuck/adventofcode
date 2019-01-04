# Advent of Code 2018 Day 4

# Data format example

# [1518-09-28 23:59] Guard #3023 begins shift
# [1518-02-20 00:40] wakes up
# [1518-08-17 00:38] falls asleep
# [1518-09-16 00:28] wakes up

import re

file = open("../inputs/Advent4", 'r')
inputs = sorted([row for row in file])

guards = {}

for line in inputs:  # Extract numeric data from inputs

    if "Guard" in line:
        match = re.search(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})] Guard #(\d{1,})', line)

        guard = match.group(6)

        if guard not in guards:
            guards[guard] = [0 for x in range(60)]

    if "asleep" in line:
        match = re.search(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})] falls asleep', line)
        asleep = int(match.group(5))

    if "wakes" in line:
        match = re.search(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})] wakes up', line)
        awake = int(match.group(5))

        for i in range(asleep, awake):
            guards[guard][i] += 1

summary = []
for guard in guards:  # Summarise minutes for each guard
    summary.append([sum(guards[guard]), guard])

summary = sorted(summary, reverse=True)

chosen = summary[0][1]  # Identify the guard with most minutes asleep

minute = guards[chosen].index(max(guards[chosen]))

summary2 = []
for guard in guards:  # Identify the minute when most often asleep
    summary.append([sum(guards[guard]), guard])

print("Part1: Sleeping Guard result is:", int(chosen) * minute)

max_qty = 0

for guard in guards:  # Find the guard with the highest total for a given minute
    if max(guards[guard]) > max_qty:
        max_qty = max(guards[guard])
        max_guard = guard
        max_minute = guards[guard].index(max_qty)
        print(max_qty, max_guard, max_minute)

print("Part2: Laziest Guard result is:", int(max_guard) * max_minute)

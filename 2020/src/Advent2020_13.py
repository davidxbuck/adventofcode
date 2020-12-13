# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/13
#
filename = ''
inps = [row.strip() for row in open(f'../inputs/Advent2020_13{filename}.txt', 'r')]
time = int(inps[0])
buses = inps[1].split(',')

# Part 1
in_service = [int(x) for x in buses if x != 'x']
next_bus_time = [(time // x + 1) * x - time for x in in_service]
print(f"AoC 2020 Day 13 Part 1 answer is: {min(next_bus_time) * in_service[next_bus_time.index(min(next_bus_time))]}")

# Part 2
offsets = {int(bus): buses.index(bus) for bus in buses if bus != 'x'}
ordered_buses = sorted(in_service, reverse=True)
period = 1
offset = 0
for bus in ordered_buses:
    next_period = 0
    for x in range(offset, 1000000000000000000000, period):
        if (x + offsets[bus]) % bus == 0:
            if next_period == 0:
                next_period = x
            else:
                offset = next_period
                period = x - next_period
                break
print(f"AoC 2020 Day 13 Part 2 answer is: {offset}")

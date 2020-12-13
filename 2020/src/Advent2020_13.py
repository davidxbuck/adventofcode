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
offsets = {bus: buses.index(str(bus)) for bus in in_service}
period = 1
offset = 0
for bus in sorted(in_service, reverse=True):
    next_offset = 0
    for x in range(offset, 1000000000000000000000, period):
        if (x + offsets[bus]) % bus == 0:
            if next_offset == 0:
                next_offset = x
            else:
                offset = next_offset
                period = x - next_offset
                break
print(f"AoC 2020 Day 13 Part 2 answer is: {offset}")

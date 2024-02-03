# Advent of Code 2023
#
# From https://adventofcode.com/2023/day/6
#


data = [x.replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(':', '').split(' ') for x in
        open('../inputs/day6.txt', 'r').read().split('\n')]
data = {x[0]: list(map(int, x[1:])) for x in data}

combinations = 1

for ix, race_time in enumerate(data['Time']):
    wins = 0
    record_distance = data['Distance'][ix]
    for hold_time in range(race_time):
        run_time = race_time - hold_time
        race_distance = run_time * hold_time
        if race_distance > record_distance:
            wins += 1
    combinations *= wins
print(f'Day 4, Part 1 {combinations}')

data = [x.replace(' ', '').split(':') for x in open('../inputs/day6.txt', 'r').read().split('\n')]
data = {x[0]: list(map(int, x[1:])) for x in data}

combinations = 1

for ix, race_time in enumerate(data['Time']):
    wins = 0
    record_distance = data['Distance'][ix]
    for hold_time in range(race_time):
        run_time = race_time - hold_time
        race_distance = run_time * hold_time
        if race_distance > record_distance:
            wins += 1
    combinations *= wins
print(f'Day 4, Part 2 {combinations}')

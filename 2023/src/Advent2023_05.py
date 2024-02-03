# Advent of Code 2023
#
# From https://adventofcode.com/2023/day/4
#



data = {x[0]: [list(map(int, y.split(' '))) for y in x[1].strip().split('\n')] for x in
        [x.split(':') for x in open('../inputs/day5.txt', 'r').read().split('\n\n')]}
seeds = data['seeds'][0]
del data['seeds']

for k, v in data.items():
    ranges = []
    for x in v:
        ranges.append((range(x[1], x[1] + x[2]), x[0] - x[1]))
    data[k] = ranges

locations = []
for seed in seeds:
    for k, v in data.items():
        found = False
        for test_range in v:
            if seed in test_range[0]:
                output_seed = seed + test_range[1]
                found = True
            if not found:
                output_seed = seed
            if found:
                # print(seed, k, test_range[0], output_seed)
                seed = output_seed
                break
    locations.append(seed)
    # print()
print(f'Day 4, Part 1 {min(locations)}')
location = 999999999999999999999
for seed_number in range(0, len(seeds), 2):
    seed_range = range(seeds[seed_number], seeds[seed_number] + seeds[seed_number + 1])
    for seed in seed_range:
        for k, v in data.items():
            found = False
            for test_range in v:
                if seed in test_range[0]:
                    output_seed = seed + test_range[1]
                    found = True
                if not found:
                    output_seed = seed
                if found:
                    # print(seed, k, test_range[0], output_seed)
                    seed = output_seed
                    break
        location = min((seed, location))
    print(f"Seed range {seed_number//2 + 1} of {len(seeds)//2} complete")
print(f'Day 4, Part 2 {location}')
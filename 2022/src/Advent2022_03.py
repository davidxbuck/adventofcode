# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/3
#
data = [''.join(set(x[:len(x) // 2]) & set(x[len(x) // 2:])) for x in
        open(f'../inputs/day3.txt', 'r').read().split('\n')]
scores = [ord(x) - 96 if ord(x) > 96 else ord(x) - 38 for x in data]
print(f'Day 3, Part 1 {sum(scores)}')

data2 = open(f'../inputs/day3.txt', 'r').read().split('\n')

data3 = [''.join(set(data2[x]) & set(data2[x + 1]) & set(data2[x + 2])) for x in range(0, len(data2), 3)]
scores2 = [ord(x) - 96 if ord(x) > 96 else ord(x) - 38 for x in data3]
print(f'Day 3, Part 2 {sum(scores2)}')

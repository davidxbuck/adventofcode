# Advent of Code 2018 Day 1

from collections import defaultdict


file = open("advent1.txt", 'r')
inputs = [int(num) for num in file]
result = sum(inputs)

print("Part 1: Sum of all inputs =", result)

running = 0
dic = defaultdict(int)
duplicate = False

while not duplicate:
    for i in inputs:
        running = running + i
        dic[running] += 1
        if dic[running] == 2:
            duplicate = True
            print("Part 2: First duplicate frequency is =", running)
            break

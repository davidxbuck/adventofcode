# Advent of Code 2018 Day 14
#

file = open("../inputs/Advent14", 'r')
recipes = int(next(file).strip())
recipelist = [int(i) for i in str(recipes)]
print("Challenge inputs:", recipes)

class Elf(object):

    def __init__(self, position):
        self.position = position

scoreboard = [3, 7]
elves = [Elf(0), Elf(1)]

loop = -1
found1 = False
found2 = False
while not (found1 & found2):
    loop += 1
    newrecipes = scoreboard[elves[0].position] + scoreboard[elves[1].position]

    first, second = divmod(newrecipes, 10)
    if first != 0:
        scoreboard.append(first)
    scoreboard.append(second)

    for elf in elves:
        elf.position = (elf.position + 1 + scoreboard[elf.position])%len(scoreboard)

    if loop > len(recipelist) and scoreboard[loop -len(recipelist) : loop] == recipelist:
        print("Part 2: Number of recipes before target sequence found:", loop -len(recipelist))
        print("Part 2: Calculated after", loop, "iterations")
        found2 = True

    if len(scoreboard) == recipes + 10:
        output = "".join([str(x) for x in scoreboard[-10:]])
        print("Part 1: Last 10 recipes out of a total of",len(scoreboard),"recipes is", output)
        print("Part 1: Calculated after", loop, "iterations")
        found1 = True










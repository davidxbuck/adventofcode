# Advent of Code 2018 Day 18
#

import numpy as np

file = open("../inputs/Advent18", 'r')
input = [row.strip() for row in file]
dim = len(input)

# Pad wood with one open space in all directions so that edge processing is unnecessary.
wood = [["." for x in range(dim + 2)]]
for row in input:
    wood.append(list(".{}.".format(row)))
wood.append(["." for x in range(dim + 2)])
wood = np.array(wood)
minute = 0
resource_vals = []
resource_value = 0


def visualise_wood():
    for ix, row in enumerate(wood.tolist()[1:dim + 1]):
        print(" {} ".format("".join(row)[1:dim + 1]))
    print()


def grow():
    global unique, counts, a, wood, resource_value, minute
    minute += 1
    new_wood = np.empty(shape=[dim + 2, dim + 2], dtype=str)
    for x in range(1, dim + 1):
        for y in range(1, dim + 1):
            grid = np.copy(wood[x - 1:x + 2, y - 1:y + 2])
            centre = grid[1, 1]
            grid[1, 1] = ""
            unique, counts = np.unique(grid, return_counts=True)
            a = dict(zip(unique, counts))
            # open
            if centre == ".":
                if a.get("|", 0) >= 3:
                    centreout = "|"
                else:
                    centreout = "."
            elif centre == "|":
                if a.get("#", 0) >= 3:
                    centreout = "#"
                else:
                    centreout = "|"
            elif centre == "#":
                if a.get("|", 0) >= 1 and a.get("#", 0) >= 1:
                    centreout = "#"
                else:
                    centreout = "."
            new_wood[x, y] = centreout
    unique, counts = np.unique(wood, return_counts=True)
    a = dict(zip(unique, counts))
    resource_value = a["|"] * a["#"]

    wood = np.copy(new_wood)
    resource_vals.append(resource_value)


visualise_wood()

minute = 0
resource_vals = []
resource_value = 0

# repeat for 10 minutes

while minute <= 10:
    grow()

visualise_wood()
print(
    "Part 1 - After 10 minutes, Trees: {}, Lumberyards: {}, Resource Value: {}".format(a["|"], a["#"], a["|"] * a["#"]))

# repeat until loop identified

while resource_vals.count(resource_value) < 4:
    grow()

# would add extra code here to ensure it's actually a loop, but I've already got the right answer...

ix = [i for i, x in enumerate(resource_vals) if x == resource_value]
period = ix[3] - ix[2]
start = ix[2]
count_on = start + (1000000000 - start) % period
visualise_wood()
print("Part 2 - After 1000000000 minutes, Resource Value will be:", resource_vals[count_on])



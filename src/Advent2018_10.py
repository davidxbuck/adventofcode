# Advent of Code 2018 Day 10

# Data format example
# position=< 52672,  52690> velocity=<-5, -5>
# position=<-20892,  10646> velocity=< 2, -1>
# position=<-10378, -52423> velocity=< 1,  5>
#
# Read file and extract dependencies

from collections import Counter

import matplotlib.pyplot as plt

file = open("../inputs2018/Advent10", 'r')
input = [row for row in file]
steps = [[int(step[10:16]), int(step[18:24]), int(step[36:38]), int(step[40:42])] for step in input]
global x, y
x = [row[0] for row in steps]
y = [row[1] for row in steps]


def move():
    in_range = 0
    for i in range(len(x)):
        x[i] += steps[i][2]
        y[i] += steps[i][3]
    count_this = [i for i in y if i < 200 and i > -200]
    count = Counter(count_this)
    if len(count) == 0:
        return 0
    else:
        return count[max(count, key=lambda k: count[k])]


def show(i):
    Y = list(map(lambda x: -x, y))
    plt.clf()
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)
    frame.axes.set_xlim(110, 180)
    frame.axes.set_ylim(-150, -100)
    frame.set_title("Iteration {}".format(i))
    plt.scatter(x, Y, marker="X")
    plt.show()


for j in range(10511):
    test = move()
    if test >= 69:  # A bit specific to this test neighbours but in general, look for convergence by the most
        # points in a single vertical line
        print(j, test)
        show(j)
print("Part1: Answer is displayed in Matplotlib output")
print("Part2: Number of seconds is", j + 1)

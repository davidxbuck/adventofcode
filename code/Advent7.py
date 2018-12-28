# Advent of Code 2018 Day 7

# Data format example
# Step D must be finished before step G can begin.
# Step A must be finished before step Y can begin.
# Step R must be finished before step O can begin.

from collections import defaultdict

# Read file and extract dependencies

file = open("Advent7.txt", 'r')
input = [row for row in file]
steps = [[step[5], step[36]] for step in sorted(input)]
first = [ord(x) - 65 for x, y in steps]
second = [ord(y) - 65 for x, y in steps]

abletorun = [False for _ in range(26)]
alreadyrun = [False for _ in range(26)]
seq = []

for x in range(26):
    # if x has no dependencies, it is ready to be run immediately
    if x in first and second.count(x) == 0:
        abletorun[x] = True
    # if x has dependencies but nothing is dependent upon it, it is the last step
    if x in second and first.count(x) == 0:
        laststep = x

# first step for the mail loop is the Alphabetically first step with no dependencies
nextstep = abletorun.index(True)
seq.append(chr(nextstep + 65))

# create dictionary of dependencies for each step
rundic = defaultdict(list)
for v, k in steps:
    rundic[ord(k) - 65].append(ord(v) - 65)

# Execution Loop

while nextstep != laststep:

    # Run step
    # For each step: Execute current step.
    # Check dependencies for all other steps to see which may be executed
    # Prime next step with alphabetically first step that is able to be run

    alreadyrun[nextstep] = True
    for key in range(26):
        if alreadyrun[key] == True:
            abletorun[key] = False
        else:
            if all(alreadyrun[x] for x in rundic[key]):
                abletorun[key] = True

            else:
                abletorun[key] = False

    nextstep = abletorun.index(True)
    seq.append(chr(nextstep + 65))

print("Part1: Assembly sequence is:", "".join(seq))

# part 2

seq = []
abletorun = [False for _ in range(26)]
alreadyrun = [False for _ in range(26)]
clock = 0
stepduration = [x for x in range(61, 87)]
nextsteps = [[None, 0] for x in range(5)]

for x in range(26):
    # if x has no dependencies, it is ready to be run immediately
    if x in first and second.count(x) == 0:
        abletorun[x] = True
    # if x has dependencies but nothing is dependent upon it, it is the last step
    if x in second and first.count(x) == 0:
        laststep = x

# prime first, up-to-five tests
count = 0
for x in range(26):
    if abletorun[x]:
        nextsteps[count][0] = x
        nextsteps[count][1] = stepduration[x]
        abletorun[x] = False
        count += 1
    if count == 5: break

# Execution Loop

while sum([nextsteps[x][1] for x in range(5)]) > 0:
    clock += 1
    # run all steps for one second. If a step finishes, record it in the alreadyrun list
    for x in range(5):
        if nextsteps[x][1] > 0:
            nextsteps[x][1] -= 1
            if nextsteps[x][1] == 0:
                alreadyrun[nextsteps[x][0]] = True
                nextsteps[x][0] = None

    # if all steps are running, loop

    if all(nextsteps[x][1] > 0 for x in range(5)):
        continue

    # Check if new steps are able to run
    alreadyrunning = [nextsteps[x][0] for x in range(5)]

    for key in range(26):
        if alreadyrun[key] == True:
            abletorun[key] = False
        else:
            if all(alreadyrun[x] for x in rundic[key]):
                abletorun[key] = True

            else:
                abletorun[key] = False

    for key in range(26):
        if abletorun[key] == True and alreadyrun[key] == False and key not in alreadyrunning:
            for i in range(5):
                if nextsteps[i][1] == 0:
                    nextsteps[i][0] = key
                    nextsteps[i][1] = stepduration[key]
                    break

print("Part2: Assembly time with 5 workers is:", clock)


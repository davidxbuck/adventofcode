# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/23
#
# Rewritten using a linked list in a dictionary.
# Deque version would have taken about 168 hours to run. This takes < 10 seconds.

starting = "469217538"
# starting = "389125467"


def prepare_list(starting, extra=0):
    CLL = {}
    cups = list(map(int, starting)) + list(range(len(starting) + 1, extra))
    for x in range(1, len(cups)):
        CLL[cups[x - 1]] = cups[x]
    CLL[cups[x]] = cups[0]
    return CLL


def move(q, current):
    removed1 = q[current]
    removed2 = q[removed1]
    removed3 = q[removed2]
    removed = [removed1, removed2, removed3]
    tail = q[removed3]
    q[current] = tail
    dest = current - 1
    while dest < 1 or dest in removed:
        if dest < 1:
            dest = max(q.keys())
        else:
            dest -= 1
    dest_tail = q[dest]
    q[dest] = removed1
    q[removed3] = dest_tail

    return q, tail


CLL = prepare_list(starting)
current = int(starting[0])
for _ in range(100):
    CLL, current = move(CLL, current)

current = 1
output = []
for x in range(8):
    current = CLL[current]
    output.append(current)

print(f"""AoC 2020 Day 23 Part 1: {"".join(list(map(str, list(output))))}""")

CLL = prepare_list(starting, 1000001)

current = int(starting[0])
for _ in range(10000000):
    CLL, current = move(CLL, current)

current = 1
num1 = CLL[current]
num2 = CLL[num1]
print(f"""AoC 2020 Day 23 Part 2: {num1 * num2}""")

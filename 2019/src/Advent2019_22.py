# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/22
#

DECK_SIZE = 10007
def main():
    with open('../inputs/Advent2019_22.txt', 'r') as f:
        # with open('../tests/testAdvent2019_22.txt', 'r') as f:
        inputs = [list(line.strip().split()) for line in f]
    commands = []
    for inp in inputs:
        if inp[0] == "cut":
            commands.append(["cut", int(inp[1])])
        elif inp[2] == "increment":
            commands.append(["increment", int(inp[3])])
        elif inp[3] == "stack":
            commands.append(["stack", 0])

    deck = list(range(DECK_SIZE))
    for cmd, val in commands:
        if cmd == "stack":
            deck.reverse()
        elif cmd == "increment":
            new_deck = deck[:]
            for x in range(DECK_SIZE):
                new_deck[x * val % DECK_SIZE] = deck[x]
            deck = new_deck[:]
        elif cmd == "cut":
            deck = deck[val:] + deck[:val]

    print(f"AoC 2019 Day 22, Part 1: {deck.index(2019)}")

if __name__ == '__main__':
    main()

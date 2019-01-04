# Advent of Code 2018 Day 9

# Data format example
# nnn players; last marble is worth nnnnn points

def play_game(players, value):
    print("Evaluating for", players, "with a last marble worth", value, "points")

    scores = {k: 0 for k in range(players + 1)}

    current_marble = 1  # position in list, not marble number
    marble = 2
    marbles = [0, 2, 1]  # populate marbles list with marbles 0-2

    while marble < value:
        if marble % 200000 == 0: print(marble)

        marble += 1

        current_player = (marble - 1) % players + 1

        if marble % 23 != 0:
            marble_add = (current_marble + 2)
            if marble_add > len(marbles): marble_add -= len(marbles)

            marbles.insert(marble_add, marble)
            current_marble = marble_add
            continue

        pop_marble = current_marble - 7
        if pop_marble < 0:
            pop_marble += len(marbles)

        current_score = marble + marbles.pop(pop_marble)

        scores[current_player] += current_score

        current_marble = pop_marble

    print("Marble of value", marble, "reached. Game over!")

    winner = max(scores, key=lambda k: scores[k])

    return winner, scores[winner]

# Read file and extract values

file = open("../inputs/Advent9", 'r')
inp = file.read().split()
players = int(inp[0])
value = int(inp[6])

winning_elf, winning_score = play_game(players, value)

print("Part1: Winner is elf", winning_elf, "with high score of:", winning_score)

winning_elf, winning_score = play_game(players, value*100)

print("Part2: Winner is elf", winning_elf, "with high score of:", winning_score)
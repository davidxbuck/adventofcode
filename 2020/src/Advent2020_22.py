# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/22
#
from math import prod


def extract_inputs(filename=''):
    data = [x.split('\n') for x in open(f'../inputs/Advent2020{filename}_22.txt', 'r').read().split('\n\n')]
    return (list(map(int, player[1:])) for player in data)


def play_1(player1, player2):
    while player1 and player2:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])
    return player1 if player1 else player2


def play_2(player1, player2):
    play_set = set()
    winner = None
    while player1 and player2:
        game = ",".join(map(str, player1)) + ':' + ",".join(map(str, player2))
        if game in play_set:
            return 1, player1, player2
        play_set.add(game)
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 <= len(player1) and card2 <= len(player2):
            winner, _, _ = play_2(player1[:card1], player2[:card2])
        elif card1 > card2:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])
    return winner, player1, player2


p1, p2 = extract_inputs()
result = play_1(p1[:], p2[:])
print(f"AoC 2020 Day 22 Part 1: {sum(prod(x) for x in zip(result, range(len(result), 0, -1)))}")

result = play_2(p1[:], p2[:])
print(f"AoC 2020 Day 22 Part 2: {sum(prod(x) for x in zip(result[result[0]], range(len(result[result[0]]), 0, -1)))}")

# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/2
#

from Advent2019_Intcode import Intcode
# Givens from the problem

NOUN = 12
VERB = 2
OUTPUT = 19690720


def iterate_noun(inputs, noun_, verb):
    for noun in range(noun_, 99):
        result = Intcode(inputs[:], noun, verb).run()
        if result >= OUTPUT:
            if result > OUTPUT:
                noun -= 1
            return noun, verb, result


def iterate_verb(inputs, noun, verb_):
    for verb in range(verb_, 99):
        result = Intcode(inputs[:], noun, verb).run()
        if result >= OUTPUT:
            if result > OUTPUT:
                verb -= 1
            return noun, verb, result


def main():
    inputs = list(map(int, [mass.strip().split(',') for mass in open('../inputs2019/Advent2019-02.txt', 'r')][0]))

    print(f'AoC 2019 Day 2, Part 1 answer is {Intcode(inputs[:], NOUN, VERB).run()}')

    # determine whether to iterate nouns or verbs first, whichever has the greatest effect on result:
    # Would be an O(2n) solution rather than a nested loop O(n**2) solution

    if Intcode(inputs[:], NOUN + 1, VERB).run() > Intcode(inputs[:], NOUN, VERB + 1).run():
        noun, verb, result = iterate_noun(inputs[:], NOUN, VERB)
        noun, verb, result = iterate_verb(inputs[:], noun, VERB)
    else:
        noun, verb, result = iterate_verb(inputs[:], NOUN, VERB)
        noun, verb, result = iterate_noun(inputs[:], NOUN, verb)
    if Intcode(inputs[:], noun, verb).run() == OUTPUT:
        print(f'AoC 2019 Day 2, Part 2 answer is {noun * 100 + verb}')
    else:
        print(f'Error')


if __name__ == '__main__':
    main()

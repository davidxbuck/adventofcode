# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/7
#

from itertools import permutations

from Advent2019_Intcode import Intcode


class Amp(object):
    def __init__(self, program, phase):
        self.amp_settings = Intcode(program[:], inp=[phase], mode='run')


def main():
    program = list(map(int, [code.strip().split(',') for code in open('../inputs2019/Advent2019_07.txt', 'r')][0]))
    max_output = 0
    for phases in permutations("43210", 5):
        next_input = 0
        for phase in phases:
            next_input, terminated = Intcode(program[:], inp=[int(phase), next_input], mode='run').run()
        if next_input > max_output:
            max_output = next_input
            answer = phases
    print(f'AoC 2019 Day 7, Part 1: Max output is: {max_output} when phases are set to {answer}')

    overall_max = -9999999999
    for phases in permutations("56789", 5):
        amps = [Amp(program, phase) for phase in map(int, phases)]
        terminated = False
        next_input = 0
        while not terminated:
            for ix, amp in enumerate(amps):
                # print(f'Amp: {ix}, Input: {next_input}, {amp.amp_settings.pointer}')
                amp.amp_settings.next_inp(next_input)
                next_input, terminated = amp.amp_settings.run()
            if not terminated:
                max_output = next_input
        if max_output > overall_max:
            # print(phases)
            # print(max_output)
            overall_max = max_output
            max_phases = phases

    print(f'AoC 2019 Day 7, Part 2: Max output is: {overall_max} when phases are set to {max_phases}')


if __name__ == '__main__':
    main()

# Advent of Code 2019
#
# From https://adventofcode.com/2019/day/23
#

import queue

from Advent2019_Intcode import Intcode


class Network(object):
    def __init__(self, program):
        self.computer = [Intcode(program[:], inp=[x], mode='network') for x in range(50)]


inputs = list(map(int, [code.strip().split(',') for code in open('../inputs/Advent2019_23.txt', 'r')][0]))

message_queues = [queue.Queue() for i in range(50)]
network = Network(inputs)
target_found = False
while not target_found:
    for computer_index in range(50):
        poll_finished = False
        while not poll_finished:
            if message_queues[computer_index].empty():
                network.computer[computer_index].next_inp(-1)
                poll_finished = True
            else:
                x, y = message_queues[computer_index].get()
                network.computer[computer_index].next_inp(x)
                network.computer[computer_index].next_inp(y)

            address, _ = network.computer[computer_index].run()

            if address != "Input":
                x, _ = network.computer[computer_index].run()
                y, _ = network.computer[computer_index].run()
            if address == 255:
                target_found = True
                print(f"AoC 2019 Day 23, Part 1: {y}")
                break
            if address != "Input":
                message_queues[address].put([x, y])

        if target_found:
            break

message_queues = [queue.Queue() for i in range(50)]
network = Network(inputs)
target_found = False
NAT = []

prev_NAT_y = 99999999999999999999

while not target_found:
    idle = True
    for computer_index in range(50):
        poll_finished = False
        while not poll_finished:
            if message_queues[computer_index].empty():
                network.computer[computer_index].next_inp(-1)
                poll_finished = True
            else:
                idle = False
                x, y = message_queues[computer_index].get()
                network.computer[computer_index].next_inp(x)
                network.computer[computer_index].next_inp(y)

            address, _ = network.computer[computer_index].run()

            if address != "Input":
                x, _ = network.computer[computer_index].run()
                y, _ = network.computer[computer_index].run()
            if address == 255:
                NAT = [x, y]
            if address != "Input" and address != 255:
                message_queues[address].put([x, y])
    if idle:
        message_queues[0].put(NAT)
        if NAT[1] == prev_NAT_y:
            print(f"AoC 2019 Day 23, Part 2: {y}")
            target_found = True
        prev_NAT_y = NAT[1]

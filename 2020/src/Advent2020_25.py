# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/25
#
filename = ''
door_pkey, card_pkey = map(int, [row.strip() for row in open(f'../inputs/Advent2020_25{filename}.txt', 'r')])
subject_no = 7
transform = 20201227

loop = 0
value = 1
door_loop = card_loop = 0
while not door_loop or not card_loop:
    loop += 1
    value *= subject_no
    value %= transform
    if value == door_pkey:
        door_loop = loop
    if value == card_pkey:
        card_loop = loop

encryption_key = 1
subject_no = door_pkey
for x in range(card_loop):
    encryption_key *= subject_no
    encryption_key %= transform

encryption_key2 = 1
subject_no = card_pkey
for x in range(door_loop):
    encryption_key2 *= subject_no
    encryption_key2 %= transform

if encryption_key == encryption_key2:
    print(f"""AoC 2020 Day 25 Part 1: {encryption_key}""")

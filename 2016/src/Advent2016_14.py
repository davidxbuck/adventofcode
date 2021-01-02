# Advent of Code 2016
#
# From https://adventofcode.com/2016/day/14
#
import hashlib
import queue

inputs = 'yjdafjpo'
# inputs = 'abc'

def find_hash():
    count = 0
    while True:
        key = hashlib.md5(bytes(inputs + str(count), encoding='utf8')).hexdigest()
        vals = set()
        for x in range(len(key) - 2):
            if key[x] == key[x + 1] == key[x + 2]:
                vals.add(key[x])
                break
        if vals:
            yield count, key, vals
        count += 1


def find_hash2():
    count = 0
    while True:
        key = hashlib.md5(bytes(inputs + str(count), encoding='utf8')).hexdigest()
        for x in range(2016):
            key = hashlib.md5(bytes(key, encoding='utf8')).hexdigest()
        vals = set()
        for x in range(len(key) - 2):
            if key[x] == key[x + 1] == key[x + 2]:
                vals.add(key[x])
                break
        if vals:
            yield count, key, vals
        count += 1


def check_for_fives(key):
    fives = set()
    for x in range(len(key) - 4):
        if key[x] == key[x + 1] == key[x + 2] == key[x + 3] == key[x + 4]:
            fives.add(key[x])
    return fives


def search(keys):
    found = 0
    possibles = {}
    found_vals = []
    while found < 64:
        count, key, vals = next(keys)
        for k in [x for x in possibles.keys() if x + 1000 < count]:
            del possibles[k]
        fives = None
        if possibles:
            fives = check_for_fives(key)
        if fives:
            possibles_copy = possibles.copy()
            for k, v in possibles.items():
                if v.intersection(fives):
                    del possibles_copy[k]
                    found += 1
                    # print(found, k, count - k, v, fives, key)
                    found_vals.append(k)
            possibles = possibles_copy.copy()
        possibles[count] = vals
    return sorted(found_vals)[63]


print(f"AoC 2016 Day 14, Part 1 answer is {search(find_hash())}")
print(f"AoC 2016 Day 14, Part 2 answer is {search(find_hash2())}")


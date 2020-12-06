# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/4
#
import re

REQUIRED_FIELDS = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']


def pass_to_dict(passport):
    return dict(field.split(':') for field in passport)


def get_passports(filename=''):
    return [pass_to_dict(" ".join(x.split('\n')).split(" ")) for x in
            open(f'../inputs2020/Advent2020_04{filename}.txt', 'r').read().split('\n\n')]


def validate_passports(passports, validation='weak'):
    if validation == 'weak':
        return sum(all(field in passport for field in REQUIRED_FIELDS) for passport in passports)
    else:
        return sum(all(field in passport and strong_validation(field, passport[field]) for field in REQUIRED_FIELDS) for
                   passport in passports)


def strong_validation(field, value):
    if field == 'byr':
        return len(value) == 4 and 1920 <= int(value) <= 2002
    if field == 'iyr':
        return len(value) == 4 and 2010 <= int(value) <= 2020
    if field == 'eyr':
        return len(value) == 4 and 2020 <= int(value) <= 2030
    if field == 'hgt':
        return ((value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193) or
                (value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76))
    if field == 'hcl':
        return bool(re.match(r'^#[a-f0-9]{6}$', value))
    if field == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if field == 'pid':
        return bool(re.match(r'^\d{9}$', value))
    return False


passports = get_passports()
print(f"""AoC 2020 Day 4 Part 1 answer is: {validate_passports(passports)}""")
print(f"""AoC 2020 Day 4 Part 2 answer is: {validate_passports(passports, validation='strong')}""")

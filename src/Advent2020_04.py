# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/4
#
import re

REQUIRED_FIELDS = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']


def pass_to_dict(passport):
    pass_dict = {}
    for field in passport:
        k, v = field.split(':')
        pass_dict[k] = v
    return pass_dict


def get_passports(filename=''):
    entries = [row for row in open(f'../inputs2020/Advent2020_04{filename}.txt', 'r')]
    passport = []
    passports = []
    for entry in entries:
        if entry != '\n':
            passport.extend(entry.strip().split(' '))
        else:
            passports.append(pass_to_dict(passport))
            passport = []
    if passport:
        passports.append(pass_to_dict(passport))
    return passports


def validate_passports(passports, validation='weak'):
    count = 0
    for passport in passports:
        valid = True
        for field in REQUIRED_FIELDS:
            if field not in passport or (validation == 'strong' and not strong_validation(field, passport[field])):
                valid = False
                break
        if valid:
            count += 1
    return count


def strong_validation(field, value):
    if field == 'byr' and len(value) == 4 and 1920 <= int(value) <= 2002:
        return True
    if field == 'iyr' and len(value) == 4 and 2010 <= int(value) <= 2020:
        return True
    if field == 'eyr' and len(value) == 4 and 2020 <= int(value) <= 2030:
        return True
    if field == 'hgt' and ((value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193) or (
            value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76)):
        return True
    if field == 'hcl' and bool(re.match(r'^#[a-f0-9]{6}$', value)):
        return True
    if field == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    if field == 'pid' and bool(re.match(r'^\d{9}$', value)):
        return True

    return False


passports = get_passports()
print(f"""AoC 2020 Day 2 Part 1 answer is: {validate_passports(passports)}""")
print(f"""AoC 2020 Day 2 Part 2 answer is: {validate_passports(passports, validation='strong')}""")

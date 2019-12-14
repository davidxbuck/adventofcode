from math import ceil


def calculate_ore(reactions, excesses, search):
    excess = dict(excesses)
    excess['FUEL'] = -search
    ore = 0
    excess['ORE'] = 0
    satisfied = False
    while not satisfied:
        satisfied = True
        for key in excess.keys():
            if key == "ORE" and excess[key] < 0:
                ore -= excess[key]
                excess[key] = 0
                continue
            if excess[key] < 0:
                satisfied = False
                mult = ceil(abs(excess[key]) / reactions[key][0])
                excess[key] += reactions[key][0] * mult
                for subkey in reactions[key][1].keys():
                    qty = reactions[key][1][subkey]
                    excess[subkey] -= qty * mult
    return ore


def main():
    with open('../inputs2019/Advent2019_14.txt', 'r') as f:
        # with open('../tests/test_Advent2019_14d.txt', 'r') as f:
        equations = [x.strip().split() for x in f]
    reactions = {}
    excesses = {}
    for equation in equations:
        result = [equation[-1], int(equation[-2])]
        inputs = {y.strip(','): int(x) for x, y in zip(equation[0:-3:2], equation[1:-3:2])}
        reactions[result[0]] = [result[1], inputs]
        excesses[result[0]] = 0
    search = 1
    print(f'AoC 2019 Day 14, Part 1: Ore consumed {calculate_ore(reactions, excesses, search)}')
    adjustment = 2 ** 40
    search = 1000000
    while adjustment > 0:
        ore = calculate_ore(reactions, excesses, search)
        if ore > 1000000000000:
            search = search - adjustment
        else:
            search = search + adjustment
        adjustment //= 2
    print(f'AoC 2019 Day 14, Part 2: Fuel produced {search}')


if __name__ == '__main__':
    main()

from math import ceil


def calculate_ore(reactions, chem_qty, fuel_required):
    chem_qty['FUEL'] = -fuel_required
    ore = 0
    satisfied = False
    while not satisfied:
        satisfied = True
        for output_chemical in chem_qty.keys():
            if output_chemical == "ORE" and chem_qty[output_chemical] < 0:
                ore -= chem_qty[output_chemical]
                chem_qty[output_chemical] = 0
                continue
            if chem_qty[output_chemical] < 0:
                satisfied = False
                output_qty, input_chemicals = reactions[output_chemical]
                batches = ceil(abs(chem_qty[output_chemical]) / output_qty)
                chem_qty[output_chemical] += output_qty * batches
                for input_chemical in input_chemicals.keys():
                    qty = input_chemicals[input_chemical]
                    chem_qty[input_chemical] -= qty * batches
    return ore


def main():
    with open('../inputs2019/Advent2019_14.txt', 'r') as f:
        equations = [x.strip().split() for x in f]
    reactions = {}
    chem_qty = {}
    for equation in equations:
        chemical, quantity = equation[-1], int(equation[-2])
        inputs = {y.strip(','): int(x) for x, y in zip(equation[0:-3:2], equation[1:-3:2])}
        reactions[chemical] = [quantity, inputs]
        chem_qty[chemical] = 0
    chem_qty['ORE'] = 0

    fuel_required = 1
    print(f'AoC 2019 Day 14, Part 1: Ore consumed {calculate_ore(reactions, chem_qty, fuel_required)}')

    adjustment = 2 ** 40
    fuel_required = 1000000
    while adjustment > 0:
        ore = calculate_ore(reactions, chem_qty, fuel_required)
        if ore > 1000000000000:
            fuel_required = fuel_required - adjustment
        else:
            fuel_required = fuel_required + adjustment
        adjustment //= 2
    print(f'AoC 2019 Day 14, Part 2: Fuel produced {fuel_required}')


if __name__ == '__main__':
    main()

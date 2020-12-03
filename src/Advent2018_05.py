# Advent of Code 2018 Day 5

def react_formula(formula):
    finished = False
    while not finished:
        update_count = 0
        updated_formula = ""
        i = 0
        while i <= len(formula)-1:
            if i >= len(formula)-1:
                updated_formula += formula[i]
                i += 1
                break
            if abs(ord(formula[i]) - ord(formula[i+1])) != 32:
                updated_formula += formula[i]
                i += 1
            else:
                update_count += 1
                i += 2
        if update_count == 0:
            finished = True
        formula = updated_formula
    return formula

file = open("../inputs2018/Advent5", 'r')
formula = next(file)
new_formula = react_formula(formula)


print("Part1: Length of formula", len(new_formula))


results = []
for j in range(65, 91):
    react_test = formula.replace(chr(j),"").replace(chr(j+32),"")
    print(chr(j), len(react_test))
    results.append(len(react_formula(react_test)))

print("Part2: Unit to remove is", chr(results.index(min(results))+65))
print("Shortest polymer is:", min(results), "units")




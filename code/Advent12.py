# Advent of Code 2018 Day 12
#

def project_growth(generations, initial):
    potsleft = 5  # add pots left and right to ensure the instructions can be followed
    potsright = 5
    pots = "." * potsleft + initial + "." * potsright
    prevanswer = 0
    prevdiff = [0]
    for j in range(generations):
        outpots = ".."
        for x in range(len(pots) - 4):
            outpots += output[rule.index(pots[x:x + 5])]
        outpots += ".."
        pots = outpots
        if pots[:5].count("#") > 0:
            pots = "....." + pots
            potsleft += 5
        if pots[-5:].count("#") > 0:
            pots = pots + "....."
            potsright += 5
        answer = 0
        for i in range(len(pots)):
            if pots[i] == "#":
                answer += (i - potsleft)
        prevdiff.append(answer - prevanswer)
        prevanswer = answer
        if j % 50 == 0 and prevdiff[-50:].count(prevdiff[-1]) == 50:
            return answer + (5*10**10-j-1) * prevdiff[-1]

    return answer


# Read file and extract initial state and patterns

file = open("Advent12.txt", 'r')
initial = next(file)[15:].strip()
next(file)
print("Initial State:", initial)

# import patterns
rules = [row.strip() for row in file]
rules = [rule.split(" => ") for rule in rules]
rule = [row[0] for row in rules]
output = [row[1] for row in rules]

generations = 20
answer = project_growth(generations, initial)
print("Part 1: Sum of pots with plants after {} generations: {}:".format(generations, answer))

generations = 5*10**10
answer = project_growth(generations, initial)
print("Part 2: Sum of pots with plants after {} generations: {}:".format(generations, answer))

# Advent of Code 2021
#
# From https://adventofcode.com/2021/day/8
#
import numpy as np
from collections import Counter

data = [row.strip().split() for row in open('../inputs/Advent2021_08.txt', 'r')]

counts = Counter(sum([list(map(len, row[11:])) for row in data], []))
print(f'Day 8, Part 1 {counts.get(2, 0) + counts.get(3, 0) + counts.get(4, 0) + counts.get(7, 0)}')

inputs = [[row[:10], row[11:]] for row in data]

segments_in = {
    0:
        """
         aaaa  
        b    c 
        b    c 
         ....  
        e    f 
        e    f 
         gggg  
        """,
    1:
        """    
         ....   
        .    c  
        .    c  
         ....   
        .    f  
        .    f  
         ....   
        """,
    2:
        """   
         aaaa  
        .    c 
        .    c 
         dddd  
        e    . 
        e    . 
         gggg
        """,
    3:
        """
         aaaa
        .    c
        .    c
         dddd
        .    f
        .    f
         gggg
        """,
    4:
        """
         ....
        b    c
        b    c
         dddd
        .    f
        .    f
         ....
        """,
    5:
        """    
         aaaa   
        b    .  
        b    .  
         dddd   
        .    f  
        .    f  
         gggg   
        """,
    6:
        """    
         aaaa   
        b    .  
        b    .  
         dddd   
        e    f  
        e    f  
         gggg   
        """,

    7:
        """    
         aaaa   
        .    c  
        .    c  
         ....   
        .    f  
        .    f  
         ....   
        """,

    8:
        """    
         aaaa   
        b    c  
        b    c  
         dddd   
        e    f  
        e    f  
         gggg
        """,
    9:
        """   
         aaaa   
        b    c  
        b    c  
         dddd   
        .    f  
        .    f  
         gggg
        """
}
segments_in = {k: set(v.strip().replace('\n', '').replace('.', '').replace(' ', '')) for k, v in segments_in.items()}

translation = {}
for in_ in range(10):
    z = []
    for not_in in range(10):
        z.append(str(len(segments_in[in_] - segments_in[not_in])))
    translation["".join(sorted(z, reverse=True))] = in_

total = 0
for inp, out in inputs:
    inp_dict = {ix: set(x) for ix, x in enumerate(inp)}
    poss = {}
    for in_ in range(10):
        for not_in in range(10):
            poss[(in_, not_in)] = inp_dict[in_] - inp_dict[not_in]

    answer = {}
    for x in range(10):
        z = []
        for y in range(10):
            z.append(str(len(poss[(x, y)])))
        answer[tuple(sorted(list(inp[x])))] = translation["".join(sorted(z, reverse=True))]

    output = ''
    for digit in out:
        output += str(answer[tuple(sorted(list(digit)))])
    output = int(output)
    total += output

print(f'Day 8, Part 2 {total}')
